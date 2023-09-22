import sounddevice as sd
from scipy.io.wavfile import write

sampling_frequency = 44100


def record_audio(duration: int = 5, file_name: str = "recording"):
    recording = sd.rec(int(duration * sampling_frequency), samplerate=sampling_frequency, channels=2)
    sd.wait()

    write(f"{file_name}.wav", sampling_frequency, recording)


record_audio()
