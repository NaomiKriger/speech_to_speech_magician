import datetime
import os

import torch
from TTS.api import TTS

TARGET_TEMP_DIR = "./TARGET"
OUTPUT_WAVS_TEMP_DIR = "./OUTPUT"
now = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")

os.makedirs(TARGET_TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_WAVS_TEMP_DIR, exist_ok=True)

output_wav_path = os.path.join(OUTPUT_WAVS_TEMP_DIR, f'output.wav')
target_wav_path = os.path.join(TARGET_TEMP_DIR, f'target.wav')
device = "cuda" if torch.cuda.is_available() else "cpu"


def get_user_input():
    input_audio_file_path = os.path.join(
        "/Users/liory/Music/Music/Media.localized/Music/Unknown_Artist/Unknown_Album/sample.wav")
    return input_audio_file_path


def clone_user_input(input_audio_file_path):
    clone_user_voice = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to(device)
    clone_user_voice.tts_to_file("This is voice cloning.", speaker_wav=input_audio_file_path, language="en",
                                 file_path=output_wav_path)

def read_gpt_response(input_audio_file_path):
    pass

# tts = TTS(
#     model_name="voice_conversion_models/multilingual/vctk/freevc24",
#     progress_bar=False)
# print("output_wav_path:", output_wav_path)
# print("target_wav_path:", target_wav_path)
# tts.voice_conversion_to_file(
#     source_wav=input_audio_file_path,
#     target_wav=target_wav_path,
#     file_path=output_wav_path)
#
# # return input_audio_file
# tts = TTS(


clone_user_input(
    input_audio_file_path="/Users/liory/Music/Music/Media.localized/Music/Unknown_Artist/Unknown_Album/sample.wav")
