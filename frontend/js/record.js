const startRecordButton = document.getElementById("startRecord");
const stopRecordButton = document.getElementById("stopRecord");
const audioPlayer = document.getElementById("audioPlayer");

let mediaRecorder;
// let audioChunks = [];
let isRecording = false;

function startRecording() {
    navigator.mediaDevices.getUserMedia({audio: true})
        .then(function (stream) {
            mediaRecorder = new MediaRecorder(stream);
            let audioChunks = [];

            mediaRecorder.ondataavailable = (event) => {
                if (event.data.size > 0) {
                    audioChunks.push(event.data);
                }
            };

            mediaRecorder.onstop = () => {
                const audioBlob = new Blob(audioChunks, {type: "audio/wav"});
                const audioUrl = URL.createObjectURL(audioBlob);
                audioPlayer.src = audioUrl;
            };

            mediaRecorder.start();
            isRecording = true;
            startRecordButton.disabled = true;
            stopRecordButton.disabled = false;
        })
        .catch(function (error) {
            console.error("Error accessing microphone:", error);
        });
}

function stopRecording() {
    if (mediaRecorder && isRecording) {
        mediaRecorder.stop();
        isRecording = false;
        startRecordButton.disabled = false;
        stopRecordButton.disabled = true;
    }
}

document.addEventListener("keydown", function (event) {
    if (event.key == " " || event.code == "Space") {
        if (!isRecording) {
            startRecording();
            console.log("START RECORDING");
        }
    }
});

document.addEventListener("keyup", function (event) {
    if (event.key == " " || event.code == "Space") {
        if (isRecording) {
            stopRecording();
            console.log("STOP RECORDING");
        }
    }
});