import {startRecording, stopRecording, isRecording, audioBlob} from "./record.js";
import {sendDataToBackend} from "./sendDataToBackend.js";
import {populateDropdown} from "./dropdown.js";

const dropdown = document.getElementById("characterDropdown");
populateDropdown(dropdown);

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

// send the .wav file + character to the backend when the button is pressed
document.addEventListener("DOMContentLoaded", function () {
    const uploadButton = document.getElementById("sendDataToBackend");
    uploadButton.addEventListener("click", function () {
        let character = dropdown.value
        console.log("CHOSEN CHARACTER: " + character);
        sendDataToBackend(audioBlob, character);
    });
});

