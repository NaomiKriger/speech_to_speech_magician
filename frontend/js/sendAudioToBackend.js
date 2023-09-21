const receiveRecordingBackendURL = "http://localhost:3000/receive_recording"

export function sendAudioToBackend(audioBlob) {
    const formData = new FormData();
    formData.append("audio", audioBlob);
    console.log("SENDING AUDIO TO SERVER");
    fetch(receiveRecordingBackendURL, {
        method: "POST",
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            console.log("TRANSCRIPT:", data.message);
        })
        .catch(error => {
            console.error("ERROR:", error);
        });
}