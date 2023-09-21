from flask import Flask, jsonify, request
from flask_cors import CORS
import openai
import datetime
import os

WAVS_TEMP_DIR = "./"

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/receive_recording", methods=["POST"])
def receive_recording():
    try:
        if "audio" in request.files:
            now = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
            wav_path = os.path.join(WAVS_TEMP_DIR, f'{now}.wav')
            request.files["audio"].save(wav_path)
            with open(wav_path, "rb") as wav_f:
                transcript = openai.Audio.transcribe("whisper-1", wav_f)
                # DO STUFF
            os.remove(wav_path)
            return jsonify({"message": transcript['text']})
        else:
            return jsonify({"error": "No 'audio' file found in the request"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
