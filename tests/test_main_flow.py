import asyncio
import unittest
from unittest.mock import Mock, patch

from main import main
from src.commons import primary_figures


class TestMainFlow(unittest.TestCase):

    @patch('main.start', Mock())
    @patch('main.text_to_speech', Mock())
    @patch('main.is_another_round')
    @patch('main.play_round')
    @patch('main.choose_figure')
    def test_one_second_round_and_new_figure(self, mock_choose_figure, mock_play_round, mock_is_another_round):
        mock_choose_figure.side_effect = [list(primary_figures.keys())[0], "SpongeBob SquarePants"]
        mock_play_round.side_effect = None
        mock_is_another_round.side_effect = ["yes", "new figure", "no"]

        asyncio.run(main())

        self.assertEqual(mock_play_round.call_count, 3)
        self.assertEqual(mock_choose_figure.call_count, 2)

    @patch('main.start', Mock())
    @patch('main.text_to_speech', Mock())
    @patch('main.is_another_round')
    @patch('main.play_round')
    @patch('main.choose_figure')
    def test_no_second_round(self, mock_choose_figure, mock_play_round, mock_is_another_round):
        mock_choose_figure.side_effect = [list(primary_figures.keys())[0]]
        mock_play_round.side_effect = None
        mock_is_another_round.side_effect = ["no"]

        asyncio.run(main())

        self.assertEqual(mock_play_round.call_count, 1)
        self.assertEqual(mock_choose_figure.call_count, 1)
