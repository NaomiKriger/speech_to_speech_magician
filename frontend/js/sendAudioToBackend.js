export function sendAudioToBackend(audioBlob) {
    const formData = new FormData();
    formData.append("audio", audioBlob);
    console.log("SENDING AUDIO TO SERVER");
    // Send the file to the backend
    fetch("http://localhost:3000/receive_recording", {
        method: "POST",
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            console.log("Response from Flask:", data);
        })
        .catch(error => {
            console.error("Error:", error);
        });
}