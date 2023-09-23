import keyboard
import numpy as np
import pygame
import sounddevice as sd
from scipy.io.wavfile import write

from src.handle_transcript import text_to_speech


def play_audio(file_path: str = "recording.wav"):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.delay(100)

    pygame.quit()


def record_audio(file_name: str = "recording"):
    sampling_frequency = 44100
    recording_started = False

    audio_data = []

    with sd.InputStream(samplerate=sampling_frequency, channels=2) as stream:
        while True:
            event = keyboard.read_event(suppress=True)
            if event and event.event_type == keyboard.KEY_DOWN:
                if not recording_started:
                    recording_started = True
                    print("Recording Started")

                audio_chunk, overflowed = stream.read(1024)
                audio_data.append(audio_chunk)

            elif event and event.event_type == keyboard.KEY_UP and recording_started:
                print("Recording stopped.")
                break

    if audio_data:
        audio_data = np.concatenate(audio_data, axis=0)
        sd.wait()
        write(f"{file_name}.wav", sampling_frequency, audio_data)
    else:
        print("No audio recorded.")

    return f"{file_name}.wav"
