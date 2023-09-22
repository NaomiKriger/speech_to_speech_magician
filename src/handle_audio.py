import asyncio
import os
import sys
import time
from threading import Thread

import keyboard
import numpy as np
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


def record_audio(file_name: str = "recording"):
    sampling_frequency = 44100
    recording_started = False

    print("Press and hold any key to start recording...")
    keyboard.read_event()
    audio_data = []

    with sd.InputStream(samplerate=sampling_frequency, channels=2) as stream:
        while True:
            event = keyboard.read_event(suppress=True)
            if event and event.event_type == keyboard.KEY_DOWN:
                if not recording_started:
                    recording_started = True
                    print("Recording started.")

                audio_chunk, overflowed = stream.read(1024)
                audio_data.append(audio_chunk)

            elif event and event.event_type == keyboard.KEY_UP and recording_started:
                print("Recording stopped.")
                break

    if audio_data:
        audio_data = np.concatenate(audio_data, axis=0)
        sd.wait()
        print(f"Recording saved as {file_name}.wav.")
        write(f"{file_name}.wav", sampling_frequency, audio_data)
    else:
        print("No audio recorded.")

    return f"{file_name}.wav"


def get_audio_sample():
    print("Let's record an audio sample of yours.")
    audio_sample_path = record_audio(file_name="sample_for_training")
    print(audio_sample_path)
    return audio_sample_path


def draw_geekcon_thread():
    word = "Loading response..."
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
