// global vars
export var notRecordingText = "Press Spacebar To Record";
export var notRecordingColor = "green";
export var recordingText = "Recording...";
export var recordingColor = "red";
const circleRadius = 200;

// initialize the canvas containing the circle
const canvas = document.getElementById("RecordCanvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
drawRecordingCircle(canvas, notRecordingColor, notRecordingText)

export function drawRecordingCircle(canvas, color, text) {
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
