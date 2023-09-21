import json
import os
import openai
import requests


def get_open_model_list():
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    open_ai_list = openai.Model.list()
    print(open_ai_list)


def make_openai_request():
    api_key = os.environ.get("OPENAI_API_KEY")
    url = 'https://api.openai.com/v1/engines/davinci/completions'
    prompt = "say a short sentence, something random"
    params = {
        "prompt": prompt,
        "max_tokens": 50,
        "temperature": 0.7
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    response = requests.post(url, headers=headers, json=params)

    data = json.loads(response.text)
    print(data)

    # print(data["choices"][0]["text"])
