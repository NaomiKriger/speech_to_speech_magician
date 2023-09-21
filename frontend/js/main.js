import {startRecording, stopRecording, isRecording, audioBlob} from "./record.js";
import {sendAudioToBackend} from "./sendAudioToBackend.js";


document.addEventListener("keydown", function (event) {
    // start recording when spacebar is pressed
    if (event.key == " " || event.code == "Space") {
        if (!isRecording) {
            startRecording();
            console.log("START RECORDING");
        }
    }
});

document.addEventListener("keyup", function (event) {
    // stop recording when spacebar is released
    if (event.key == " " || event.code == "Space") {
        if (isRecording) {
            stopRecording();
            console.log("STOP RECORDING");
        }
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const uploadButton = document.getElementById("sendAudioToBackend");
    // uploadButton.addEventListener("click", sendAudioToBackend(audioBlob));

    uploadButton.addEventListener("click", function () {
        sendAudioToBackend(audioBlob);
    });
});
