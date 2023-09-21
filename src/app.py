from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/receive_recording", methods=["POST"])
def receive_recording():
    try:
        if "audio" in request.files:
            audio_file = request.files["audio"]
            print(audio_file) # You can process the audio file here (e.g., save it to disk, perform analysis, etc.)
            return jsonify({"message": "WAV file received and processed successfully"})
        else:
            return jsonify({"error": "No 'audio' file found in the request"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
