import unittest
from unittest.mock import Mock, patch

from src.handle_audio import play_audio


class TestPlayAudio(unittest.TestCase):

    @patch("src.handle_audio.pygame")
    def test_play_audio(self, mock_pygame):
        mock_init = Mock()
        mock_mixer_init = Mock()
        mock_music_load = Mock()
        mock_music_play = Mock()
        mock_get_busy = Mock()
        mock_time_delay = Mock()

        mock_pygame.init.return_value = mock_init
        mock_pygame.mixer.init.return_value = mock_mixer_init
        mock_pygame.mixer.music.load.return_value = mock_music_load
        mock_pygame.mixer.music.play.return_value = mock_music_play
        mock_pygame.mixer.music.get_busy.side_effect = [True, False]  # Simulate busy then not busy
        mock_pygame.time.delay.return_value = mock_time_delay

        play_audio(file_path="test.wav")

        mock_pygame.init.assert_called_once()
        mock_pygame.mixer.init.assert_called_once()
        mock_pygame.mixer.music.load.assert_called_once_with("test.wav")
        mock_pygame.mixer.music.play.assert_called_once()
        mock_pygame.mixer.music.get_busy.assert_called_with()
        mock_pygame.time.delay.assert_called_with(100)
        mock_pygame.quit.assert_called_once()
