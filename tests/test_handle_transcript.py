import unittest
from unittest.mock import MagicMock, Mock, patch

from src.handle_transcript import ChatCompletion, get_gpt_response, make_openai_request


class TestGetGptResponse(unittest.TestCase):
    @patch("src.handle_transcript.make_openai_request")
    @patch("src.handle_transcript.get_system_instructions", return_value="System instructions")
    def test_successful_request(
            self, mock_get_system_instructions, mock_make_openai_request
    ):
        mock_response = Mock()
        mock_response.choices = [Mock(message={"content": "Mock AI response"})]
        mock_make_openai_request.return_value = mock_response

        transcript = "What's the weather like?"
        chosen_figure = "Homer Simpson"

        result = get_gpt_response(transcript, chosen_figure)

        mock_get_system_instructions.assert_called_once_with(chosen_figure)
        mock_make_openai_request.assert_called_once_with(
            system_instructions="System instructions", user_question=transcript
        )
        self.assertEqual(result, "Mock AI response")

    @patch("src.handle_transcript.make_openai_request")
    @patch("src.handle_transcript.get_system_instructions", return_value="System instructions")
    def test_request_exception(
            self, mock_get_system_instructions, mock_make_openai_request
    ):
        mock_make_openai_request.side_effect = Exception("Request failed")

        transcript = "What's the weather like?"
        chosen_figure = "Homer Simpson"

        result = get_gpt_response(transcript, chosen_figure)

        mock_get_system_instructions.assert_called_once_with(chosen_figure)
        mock_make_openai_request.assert_called_once_with(
            system_instructions="System instructions", user_question=transcript
        )
        self.assertEqual(result, "Request failed")


class TestMakeOpenAIRequest(unittest.TestCase):
    @patch("src.handle_transcript.os.environ", {"OPENAI_API_KEY": "some_api_key"})
    @patch("src.handle_transcript.openai.ChatCompletion.create")
    def test_make_openai_request(self, mock_create):
        mock_completion = MagicMock(spec=ChatCompletion)
        mock_completion.choices = [MagicMock(message={"content": "Mock AI response"})]

        mock_create.return_value = mock_completion

        system_instructions = "System instructions"
        user_question = "User question"
        result = make_openai_request(system_instructions, user_question)

        self.assertIsInstance(result, ChatCompletion)
        self.assertEqual(result.choices[0].message["content"], "Mock AI response")
        mock_create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_instructions},
                {"role": "user", "content": user_question},
            ],
            max_tokens=50,
        )
