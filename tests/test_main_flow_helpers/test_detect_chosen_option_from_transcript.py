import unittest

from src.main_flow_helpers import detect_chosen_option_from_transcript


class TestDetectChosenOptionFromTranscript(unittest.TestCase):
    def test_exact_match(self):
        transcript = "SpongeBob SquarePants"
        options = ["SpongeBob SquarePants", "Homer Simpson", "Pikachu"]
        result = detect_chosen_option_from_transcript(transcript, options)
        self.assertEqual(result, "SpongeBob SquarePants")

    def test_partial_match(self):
        transcript = "SpongeBob"
        options = ["SpongeBob SquarePants", "Homer Simpson", "Pikachu"]
        result = detect_chosen_option_from_transcript(transcript, options)
        self.assertEqual(result, "SpongeBob SquarePants")

    def test_no_match(self):
        transcript = "SpongeBob"
        options = ["Homer Simpson", "Pikachu", "Shrek"]
        result = detect_chosen_option_from_transcript(transcript, options)
        self.assertEqual(result, "")

    def test_multiple_options_with_best_match(self):
        transcript = "Sponge"
        options = ["SpongeBob SquarePants", "SpongeBob", "Sponge"]
        result = detect_chosen_option_from_transcript(transcript, options)
        self.assertEqual(result, "Sponge")

    def test_no_transcript(self):
        transcript = ""
        options = ["SpongeBob SquarePants"]
        result = detect_chosen_option_from_transcript(transcript, options)
        self.assertEqual(result, "")
