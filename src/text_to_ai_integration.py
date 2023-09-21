import os

import openai


def get_open_model_list():
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    open_ai_list = openai.Model.list()
    print(open_ai_list)


def make_openai_request():
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You provide funny answers"},
            {"role": "user", "content": "What does Harry Potter like in Hogwarts?"}
        ],
        max_tokens=20
    )

    return completion.choices[0].message["content"]


if __name__ == "__main__":
    make_openai_request()
