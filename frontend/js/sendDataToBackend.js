const receiveRecordingBackendURL = "http://localhost:3000/receive_recording"

export function sendDataToBackend(audioBlob, character) {
    const formData = new FormData();
    formData.append("audio", audioBlob);
    formData.append("character", character);
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