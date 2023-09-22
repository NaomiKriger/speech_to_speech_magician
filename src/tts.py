from TTS.api import TTS

output_audio_path = "output.wav"


def text_to_speech():
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=True)
    tts.voice_conversion_to_file(source_wav="my/source.wav", target_wav="my/target.wav", file_path="output.wav")


if __name__ == "__main__":
    text_to_speech()