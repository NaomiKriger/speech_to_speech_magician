import asyncio
import os
import sys
import time
from threading import Thread

import openai
import pyttsx3
from openai import ChatCompletion

from src.commons import get_system_instructions, Gender


def print_text_when_waiting_for_transcription(text_to_draw: str):
    word = f"{text_to_draw}..."
    for i in range(len(word)):
        sys.stdout.write("\r" + word[:i + 1] + " " * (len(word) - i - 1))
        sys.stdout.flush()
        time.sleep(0.2)
    print()


async def get_transcript(audio_file_path: str, text_to_draw_while_waiting: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    audio_file = open(audio_file_path, "rb")
    transcript = None

    async def transcribe_audio():
        nonlocal transcript
        try:
            response = openai.Audio.transcribe(model="whisper-1", file=audio_file, language="en")
            transcript = response.get("text")
        except Exception as e:
            print(e)

    draw_thread = Thread(target=print_text_when_waiting_for_transcription(text_to_draw_while_waiting))
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
        max_tokens=50
    )

    return completion


def text_to_speech(text: str, gender: str = Gender.female.value):
    engine = pyttsx3.init()

    engine.setProperty("rate", 180)  # Speed of speech (words per minute)
    voices = engine.getProperty('voices')
    voice_id = voices[0].id if gender == "male" else voices[1].id
    engine.setProperty("voice", voice_id)

    engine.say(text)
    engine.runAndWait()
