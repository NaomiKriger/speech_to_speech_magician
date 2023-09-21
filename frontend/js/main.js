import {startRecording, stopRecording, isRecording, audioBlob} from "./record.js";
import {sendAudioToBackend} from "./sendAudioToBackend.js";


// start recording when spacebar is pressed
document.addEventListener("keydown", function (event) {
    if (event.key == " " || event.code == "Space") {
        if (!isRecording) {
            startRecording();
            console.log("START RECORDING");
        }
    }
});

// stop recording when spacebar is released
document.addEventListener("keyup", function (event) {
    if (event.key == " " || event.code == "Space") {
        if (isRecording) {
            stopRecording();
            console.log("STOP RECORDING");
        }
    }
});

// send the .wav file to the backend when the button is pressed
document.addEventListener("DOMContentLoaded", function () {
    const uploadButton = document.getElementById("sendAudioToBackend");
    uploadButton.addEventListener("click", function () {
        sendAudioToBackend(audioBlob);
    });
});
