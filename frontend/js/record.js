const startRecordButton = document.getElementById("startRecord");
const stopRecordButton = document.getElementById("stopRecord");
const audioPlayer = document.getElementById("audioPlayer");

let mediaRecorder;
let audioChunks = [];

startRecordButton.addEventListener("click", startRecording);
stopRecordButton.addEventListener("click", stopRecording);

async function startRecording() {
    const stream = await navigator.mediaDevices.getUserMedia({audio: true});

    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
            audioChunks.push(event.data);
        }
    };

    mediaRecorder.onstop = () => {
        // const audioBlob = new Blob(audioChunks, {type: "audio/ogg; codecs=opus"});
        const audioBlob = new Blob(audioChunks, {type: "audio/wav"});
        const audioUrl = URL.createObjectURL(audioBlob);
        audioPlayer.src = audioUrl;
    };

    mediaRecorder.start();
    startRecordButton.disabled = true;
    stopRecordButton.disabled = false;
}

function stopRecording() {
    if (mediaRecorder && mediaRecorder.state === "recording") {
        mediaRecorder.stop();
        startRecordButton.disabled = false;
        stopRecordButton.disabled = true;
    }
}