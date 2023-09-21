// global vars
import {recordingText, recordingColor, notRecordingText, notRecordingColor, drawRecordingCircle} from "./drawCircle.js";

// initialize stuff
const audioPlayer = document.getElementById("audioPlayer"); // TODO - remove this
let mediaRecorder;
export let audioBlob = null;
export let isRecording = false;

// initialize the recording canvas
const canvas = document.getElementById("RecordCanvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
drawRecordingCircle(canvas, notRecordingColor, notRecordingText)

export function startRecording() {
    audioBlob = null;
    // modify canvas
    drawRecordingCircle(canvas, recordingColor, recordingText)
    // record
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
                audioBlob = new Blob(audioChunks, {type: "audio/wav"});
                const audioUrl = URL.createObjectURL(audioBlob); // TODO - delete this
                audioPlayer.src = audioUrl; // TODO - delete this
            };

            mediaRecorder.start();
            isRecording = true;
        })
        .catch(function (error) {
            console.error("Error accessing microphone:", error);
        });
}

export function stopRecording() {
    // modify canvas
    drawRecordingCircle(canvas, notRecordingColor, notRecordingText)
    // stop recording
    if (mediaRecorder && isRecording) {
        mediaRecorder.stop();
        isRecording = false;
    }
}

