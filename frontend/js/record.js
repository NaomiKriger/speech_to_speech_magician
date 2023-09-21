const audioPlayer = document.getElementById("audioPlayer");

// initialize the recording canvas
const canvas = document.getElementById("RecordCanvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
modifyRecordCanvas(canvas, "green", "Press Spacebar To Record")

let mediaRecorder;
let isRecording = false;

function startRecording() {
    modifyRecordCanvas(canvas, "red", "Recording...")

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
    modifyRecordCanvas(canvas, "green", "Press Spacebar To Record")

    if (mediaRecorder && isRecording) {
        mediaRecorder.stop();
        isRecording = false;
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


function modifyRecordCanvas(canvas, color, text) {

    // Check if the canvas element is supported
    const ctx = canvas.getContext("2d");
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = 200;

    // add color
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
    ctx.fill();

    // add text
    ctx.fillStyle = "white";
    ctx.font = "20px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(text, centerX, centerY);

}
