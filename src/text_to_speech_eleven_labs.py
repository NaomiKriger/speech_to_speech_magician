import os

import requests

voice_id_rachel = "21m00Tcm4TlvDq8ikWAM"
voice_id_dave = "CYw3kZ02Hs0563khs1Fj"

CHUNK_SIZE = 1024
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id_dave}"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": os.environ.get("ELEVEN_LABS_API_KEY")
}

data = {
  "text": "Hi! My name is Bella, nice to meet you!",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
