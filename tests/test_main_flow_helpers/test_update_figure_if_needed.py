import unittest
from unittest.mock import Mock, patch

from src.main_flow_helpers import update_figure_if_needed


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
