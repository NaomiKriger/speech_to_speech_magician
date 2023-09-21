import datetime
import os

import openai
from flask import Flask, jsonify, request, session
from flask_cors import CORS

WAVS_TEMP_DIR = "./"

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


def render_template(some_input: str, figure=None):
    return "hi"


@app.route("/receive_recording", methods=["POST"])
def receive_recording():

    try:
        if "start_button" in request.form:
            # User clicked "Start" button, show figure selection form
            return render_template("figure_selection.html")

        elif "choose_figure_button" in request.form:
            # User submitted figure selection form
            chosen_figure = request.form.get("figure")

            # Store the chosen figure in the user's session
            session["chosen_figure"] = chosen_figure

            return render_template("question_recording.html", figure=chosen_figure)

        elif "audio" in request.files:
            now = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
            wav_path = os.path.join(WAVS_TEMP_DIR, f'{now}.wav')
            request.files["audio"].save(wav_path)
            character = request.form['character']  # TODO - use it
            with open(wav_path, "rb") as wav_f:
                transcript = openai.Audio.transgcribe("whisper-1", wav_f)
                # DO STUFF
            os.remove(wav_path)
            return jsonify({"message": transcript['text']})

        elif "finish_button" in request.form:
            # User clicked "Finish" button, clear the chosen figure and close the session
            session.pop("chosen_figure", None)
            return render_template("figure_selection.html")

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
