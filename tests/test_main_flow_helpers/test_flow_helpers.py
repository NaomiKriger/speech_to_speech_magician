import unittest
from unittest.mock import patch

import pytest

from src.commons import primary_figures
from src.main_flow_helpers import ask_a_question, title, welcome_prompt, start, play_round, is_another_round


class TestStart(unittest.TestCase):

    @patch("src.main_flow_helpers.main_gui.create_title")
    @patch("src.main_flow_helpers.print")
    @patch("src.main_flow_helpers.text_to_speech")
    def test_start(self, mock_text_to_speech, mock_print, mock_create_title):
        start()

        mock_create_title.assert_called_once_with(title)
        mock_print.assert_called_once_with(welcome_prompt)
        mock_text_to_speech.assert_called_once_with(welcome_prompt)


class TestAskAQuestion(unittest.TestCase):

    @patch("src.main_flow_helpers.print")
    @patch("src.main_flow_helpers.text_to_speech")
    @patch("src.main_flow_helpers.record_audio", return_value="user_question.wav")
    def test_ask_a_question(self, mock_record_audio, mock_text_to_speech, mock_print):
        file_name = "chosen_figure.wav"
        chosen_figure = list(primary_figures.keys())[0]
        message = f"Press + hold an arrow key to start talking to {chosen_figure}"

        result = ask_a_question(file_name, chosen_figure)

        mock_print.assert_called_once_with(message)
        mock_text_to_speech.assert_called_once_with(message)
        mock_record_audio.assert_called_once_with(file_name=file_name)

        self.assertEqual(result, "user_question.wav")


chosen_figure_play_round = list(primary_figures.keys())[0]


@pytest.mark.asyncio
@patch("src.main_flow_helpers.ask_a_question")
@patch("src.main_flow_helpers.get_transcript")
@patch("src.main_flow_helpers.print")
@patch("src.main_flow_helpers.get_system_instructions")
@patch("src.main_flow_helpers.make_openai_request")
@patch("src.main_flow_helpers.text_to_speech")
async def test_play_round(mock_text_to_speech, mock_make_openai_request, mock_get_system_instructions, mock_print,
                          mock_get_transcript, mock_ask_a_question):
    user_chosen_path = "user_question.wav"
    mock_ask_a_question.return_value = user_chosen_path
    transcription = "How are you?"
    mock_get_transcript.return_value = transcription

    await play_round(chosen_figure_play_round)

    system_instructions = mock_get_system_instructions(chosen_figure_play_round)
    gpt_answer = \
        mock_make_openai_request(system_instructions=system_instructions, user_question=transcription).choices[
            0].message[
            "content"]

    mock_print.assert_any_call(f"You said: {transcription}")
    mock_print.assert_any_call(f"answer from {chosen_figure_play_round}: {gpt_answer}")
    mock_get_transcript.assert_called_once_with(audio_file_path=user_chosen_path,
                                                text_to_draw_while_waiting="Loading response")
    mock_ask_a_question.assert_called_once_with(file_name="user_question", chosen_figure=chosen_figure_play_round)
    mock_text_to_speech.assert_called_once_with(text=gpt_answer, gender=primary_figures.get(chosen_figure_play_round))


@pytest.mark.asyncio
@patch("src.main_flow_helpers.print")
@patch("src.main_flow_helpers.text_to_speech")
@patch("src.main_flow_helpers.record_audio")
@patch("src.main_flow_helpers.get_transcript")
@patch("src.main_flow_helpers.detect_chosen_option_from_transcript")
async def test_is_another_round(mock_detect_chosen_option_from_transcript, mock_get_transcript, mock_record_audio,
                                mock_text_to_speech, mock_print):
    ask_if_play_another_round = "Do you want to play another round? Say 'yes' or 'no'. \n" \
                                "Say 'new figure' to choose a new figure"

    mock_record_audio.return_value = "is_another_round.wav"
    mock_get_transcript.return_value = "some transcript"
    mock_detect_chosen_option_from_transcript.return_value = "no"
    result = await is_another_round()

    mock_print.assert_any_call(ask_if_play_another_round)
    mock_print.assert_any_call(f"You said: {mock_get_transcript.return_value}")
    mock_text_to_speech.assert_called_once_with(ask_if_play_another_round)

    assert result == mock_detect_chosen_option_from_transcript.return_value

    # CALL is_another_round() AGAIN, NOW WITH A DIFFERENT VALUE FOR detect_chosen_option_from_transcript()
    mock_detect_chosen_option_from_transcript.return_value = ""
    result = await is_another_round()

    assert result == "yes"
