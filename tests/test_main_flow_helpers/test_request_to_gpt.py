import unittest

from dotenv import load_dotenv
from openai import ChatCompletion
from openai.openai_object import OpenAIObject

from src.commons import get_system_instructions
from src.handle_transcript import make_openai_request

load_dotenv()


# NOTE - MAKING A REAL CALL TO GPT, NEED TO PATCH THIS
class TestGptRequest(unittest.TestCase):

    @unittest.skip("making real API call")
    def test_gpt_request(self):
        res = make_openai_request(system_instructions=get_system_instructions(figure="drunk future teller"),
                                  user_question="What does Harry Potter like in Hogwarts?")

        assert isinstance(res.choices[0].message["content"], str)
        self.assertTrue(isinstance(res, ChatCompletion) or isinstance(res, OpenAIObject))
