// global vars
var notRecordingText = "Press Spacebar To Record";
var notRecordingColor = "green";
var recordingText = "Recording...";
var recordingColor = "red";
var circleRadius = 200;

// initialize stuff
let mediaRecorder;
let isRecording = false;
const audioPlayer = document.getElementById("audioPlayer"); // TODO - remove this

// initialize the recording canvas
const canvas = document.getElementById("RecordCanvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
drawRecordingCircle(canvas, notRecordingColor, notRecordingText)

function startRecording() {
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
                const audioBlob = new Blob(audioChunks, {type: "audio/wav"});
                const audioUrl = URL.createObjectURL(audioBlob);
                audioPlayer.src = audioUrl;
            };

            mediaRecorder.start();
            isRecording = true;
        })
        .catch(function (error) {
            console.error("Error accessing microphone:", error);
        });
}

function stopRecording() {
    // modify canvas
    drawRecordingCircle(canvas, notRecordingColor, notRecordingText)
    // stop recording
    if (mediaRecorder && isRecording) {
        mediaRecorder.stop();
        isRecording = false;
    }
}

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


function drawRecordingCircle(canvas, color, text) {
    const ctx = canvas.getContext("2d");
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;

    // add color
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(centerX, centerY, circleRadius, 0, 2 * Math.PI);
    ctx.fill();

    // add text
    ctx.fillStyle = "white";
    ctx.font = "25px Lucida Console";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(text, centerX, centerY);

}
