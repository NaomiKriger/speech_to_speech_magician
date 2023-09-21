import os

import openai


def get_open_model_list():
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    open_ai_list = openai.Model.list()
    print(open_ai_list)


def make_openai_request(system_instruction: str, user_question: str):
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_question}
        ],
        max_tokens=20
    )

    return completion.choices[0].message["content"]
