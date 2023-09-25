import unittest
from unittest.mock import Mock, patch

import pytest

from src.commons import primary_figures
from src.main_flow_helpers import choose_figure, get_figure_from_recording, update_figure_if_needed


class TestUpdateFigureIfNeeded(unittest.TestCase):
    @patch("src.main_flow_helpers.text_to_speech", Mock())
    @patch("src.main_flow_helpers.choose_random_figure", return_value="Shrek")
    def test_figure_updated_when_none(self, mock_choose_random_figure):
        result = update_figure_if_needed("")
        self.assertEqual(result, "Shrek")
        mock_choose_random_figure.assert_called_once()

    @patch("src.main_flow_helpers.text_to_speech", Mock())
    @patch("src.main_flow_helpers.choose_random_figure", return_value="Pikachu")
    def test_figure_not_updated_when_provided(self, mock_choose_random_figure):
        result = update_figure_if_needed("Steve Jobs")
        self.assertEqual(result, "Steve Jobs")
        mock_choose_random_figure.assert_not_called()


@pytest.mark.asyncio
async def test_get_figure_from_recording():
    figures_names = primary_figures
    figure_per_transcript = "fortune teller"
    actual_figure_to_use = "drunk fortune teller"
    file_name = "chosen_figure"
    with patch("src.main_flow_helpers.record_audio") as mock_record_audio, patch(
            "src.main_flow_helpers.get_transcript"
    ) as mock_get_transcript, patch(
        "src.main_flow_helpers.detect_chosen_option_from_transcript"
    ) as mock_detect_chosen_option, patch(
        "src.main_flow_helpers.update_figure_if_needed"
    ) as mock_update_figure:
        mock_record_audio.return_value = f"{file_name}.wav"
        mock_get_transcript.return_value = figure_per_transcript
        mock_detect_chosen_option.return_value = actual_figure_to_use
        mock_update_figure.return_value = actual_figure_to_use

        result = await get_figure_from_recording(figures_names)

        assert result == actual_figure_to_use
        mock_record_audio.assert_called_once_with(file_name=file_name)
        mock_get_transcript.assert_called_once_with(audio_file_path=f"{file_name}.wav",
                                                    text_to_draw_while_waiting="Getting your chosen figure")
        mock_detect_chosen_option.assert_called_once_with(transcript=figure_per_transcript, options=figures_names)
        mock_update_figure.assert_called_once_with(figure=actual_figure_to_use)


@pytest.mark.asyncio
@patch("src.main_flow_helpers.get_figure_from_recording", return_value=list(primary_figures.keys())[0])
@patch("src.main_flow_helpers.text_to_speech")
async def test_choose_figure(mock_text_to_speech, mock_get_figure_from_recording):
    result = await choose_figure()

    mock_text_to_speech.assert_any_call("Who do you want to talk to?")
    mock_text_to_speech.assert_any_call("say the figure's name")
    mock_get_figure_from_recording.assert_called_once()
    assert result == list(primary_figures.keys())[0]
