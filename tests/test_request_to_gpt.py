import unittest

from dotenv import load_dotenv

from src.commons import constant_instruction
from src.text_to_ai_integration import make_openai_request

load_dotenv()


# NOTE - MAKING A REAL CALL TO GPT, NEED TO PATCH THIS
class TestGptRequest(unittest.TestCase):
    chosen_figure_by_user = "drunk future teller"
    request_based_instruction = f" You are: {chosen_figure_by_user}"
    user_question = "What does Harry Potter like in Hogwarts?"

    def test_gpt_request(self):
        res = make_openai_request(system_instruction=constant_instruction + self.request_based_instruction,
                                  user_question=self.user_question)
        assert res is not None
