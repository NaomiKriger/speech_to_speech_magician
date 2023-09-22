import os

import openai
from openai import ChatCompletion

from src.commons import get_system_instructions


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
