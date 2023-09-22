import asyncio
import os
import sys
import time
from threading import Thread

import openai
import pygame
import sounddevice as sd
from scipy.io.wavfile import write


def play_audio(file_name: str = "recording.wav"):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.delay(100)

    pygame.quit()


def play_audio_response(transcript: str):
    play_audio("audio_response.wav")
    return "playing response"


def record_audio(duration: int = 5, file_name: str = "recording"):
    sampling_frequency = 44100
    print("starting to record")
    recording = sd.rec(int(duration * sampling_frequency), samplerate=sampling_frequency, channels=2)
    sd.wait()

    print("finished recording")
    write(f"{file_name}.wav", sampling_frequency, recording)
    return f"{file_name}.wav"


def get_audio_sample():
    duration = 5
    print("Let's record an audio sample of yours. Press any key to start your recording. "
          f"\nYou will have {duration} seconds to record once you press a key")
    input("\nPress any key to start recording")

    # TODO: increase duration to 10 seconds
    audio_sample_path = record_audio(duration=duration, file_name="sample_for_training")
    print(audio_sample_path)
    return audio_sample_path


def draw_geekcon_thread():
    word = "Loading your response..."
    for i in range(len(word) + 1):
        sys.stdout.write("\r" + "." * i + word[i:])
        sys.stdout.flush()
        time.sleep(0.2)
    print()


async def get_transcript_async(audio_path: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    audio_file = open(audio_path, "rb")
    transcript = None

    async def transcribe_audio():
        nonlocal transcript
        try:
            response = openai.Audio.transcribe("whisper-1", audio_file)
            transcript = response.get("text")
        except Exception as e:
            print(e)

    draw_thread = Thread(target=draw_geekcon_thread)
    draw_thread.start()

    transcription_task = asyncio.create_task(transcribe_audio())
    await transcription_task

    if transcript is None:
        print("Transcription not available within the specified timeout.")

    print(f"\n{transcript}")
    return transcript
