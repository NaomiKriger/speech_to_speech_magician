import unittest

from dotenv import load_dotenv

from src.commons import get_system_instructions
from src.text_to_ai_integration import make_openai_request

load_dotenv()


# NOTE - MAKING A REAL CALL TO GPT, NEED TO PATCH THIS
class TestGptRequest(unittest.TestCase):

    def test_gpt_request(self):
        res = make_openai_request(system_instruction=get_system_instructions(figure="drunk future teller"),
                                  user_question="What does Harry Potter like in Hogwarts?")
        assert res is not None
