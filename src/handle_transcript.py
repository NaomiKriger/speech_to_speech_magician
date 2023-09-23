import asyncio
import os
import sys
import time
from io import BytesIO
from threading import Thread

import openai
import pygame
from gtts import gTTS
from openai import ChatCompletion

from src.commons import get_system_instructions


def draw_geekcon_thread():
    word = "Loading response..."
    for i in range(len(word) + 1):
        sys.stdout.write("\r" + "." * i + word[i:])
        sys.stdout.flush()
        time.sleep(0.2)
    print()


async def get_transcript(audio_file_path: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    audio_file = open(audio_file_path, "rb")
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


def get_gpt_response(transcript: str, chosen_figure: str) -> str:
    system_instructions = get_system_instructions(chosen_figure)
    try:
        return make_openai_request(
            system_instructions=system_instructions, user_question=transcript).choices[0].message["content"]
    except Exception as e:
        return e.args[0]


def make_openai_request(system_instructions: str, user_question: str) -> ChatCompletion:
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": user_question}
        ],
        max_tokens=20
    )

    return completion


def text_to_speech(text: str):
    speech = gTTS(text, lang='en', lang_check=False, slow=False)

    speech_bytes = BytesIO()
    speech.write_to_fp(speech_bytes)
    speech_bytes.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(speech_bytes)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue
