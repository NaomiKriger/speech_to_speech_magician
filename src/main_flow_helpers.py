import random
from typing import List

from fuzzywuzzy import fuzz

from gui import main_gui
from src.commons import primary_figures, fallback_figures
from src.handle_audio import record_audio
from src.handle_transcript import text_to_speech, get_transcript, get_gpt_response

title = "Speech to Speech Magician"
welcome_prompt = "Hello! Welcome to the speech-to-speech magician! Good to see you here.\n" \
                 "Whenever you'll be asked to talk - press and hold an arrow key while talking."


def start() -> None:
    main_gui.create_title(title)
    print(welcome_prompt)
    text_to_speech(welcome_prompt)


def detect_chosen_option_from_transcript(
        transcript: str, options: List[str]) -> str:
    best_match_score = 0
    best_match = ""

    for option in options:
        score = fuzz.token_set_ratio(transcript.lower(), option.lower())
        if score > best_match_score:
            best_match_score = score
            best_match = option

    if best_match_score >= 70:
        return best_match
    else:
        return ""


def choose_random_figure(figures_for_user: list) -> str:
    return random.choice(figures_for_user)


def update_figure_if_needed(figure: str) -> str:
    if not figure:
        figure = choose_random_figure(list(fallback_figures.keys()))
        message = "Ohhh too bad... seems you said something that isn't on our list...\n" \
                  "No problem. We'll choose a figure for you!\n" \
                  f"Your chosen figure is...{figure}"
        print(message)
        text_to_speech(message)
    else:
        message = f"You have chosen: {figure}"
        print(message)
        text_to_speech(message)
    return figure


async def get_figure_from_recording(figures_names: list) -> str:
    file_name = "chosen_figure"
    record_audio(file_name=file_name)
    transcript = await get_transcript(audio_file_path=f"{file_name}.wav",
                                      text_to_draw_while_waiting="Getting your chosen figure")
    print(f"audio detected: {transcript}")
    figure = detect_chosen_option_from_transcript(transcript=transcript, options=figures_names)
    figure = update_figure_if_needed(figure=figure)

    return figure


async def choose_figure() -> str:
    message = "Who do you want to talk to?"
    print(f"\n\n{message}")
    text_to_speech(message)

    figure_options = list(primary_figures.keys())
    for _, option in enumerate(figure_options, start=1):
        print(f"{option}")

    message = "say the figure's name"
    print(f"\n{message}")
    text_to_speech(message)
    figure = await get_figure_from_recording(figure_options)
    return figure


def ask_a_question(file_name: str, chosen_figure: str) -> str:
    message = f"Press + hold an arrow key to start talking to {chosen_figure}"
    print(message)
    text_to_speech(message)

    user_question_path = record_audio(file_name=file_name)
    return user_question_path


async def play_round(chosen_figure: str) -> None:
    user_question_path = ask_a_question(file_name="user_question", chosen_figure=chosen_figure)
    # TODO: wrap here in try<->except
    transcription = await get_transcript(audio_file_path=user_question_path,
                                         text_to_draw_while_waiting="Loading response")
    print(f"You said: {transcription}")
    # TODO: decide how to handle an error here. maybe try one more time and then quit the game
    # TODO: the "quit" logic is in the outer function. here we provide a "sorry" message
    gpt_answer = get_gpt_response(transcript=transcription, chosen_figure=chosen_figure)
    print(f"answer from {chosen_figure}: {gpt_answer}")
    gender = primary_figures.get(chosen_figure) if chosen_figure in primary_figures \
        else fallback_figures.get(chosen_figure)
    text_to_speech(text=gpt_answer, gender=gender)


async def is_another_round() -> str:
    ask_if_play_another_round = "Do you want to play another round? Say 'yes' or 'no'. \n" \
                                "Say 'new figure' to choose a new figure"
    print(ask_if_play_another_round)
    text_to_speech(ask_if_play_another_round)
    is_another_round_recording_path = record_audio(file_name="is_another_round")
    transcript = await get_transcript(audio_file_path=f"{is_another_round_recording_path}",
                                      text_to_draw_while_waiting="Getting your choice")
    print(f"You said: {transcript}")
    choice = detect_chosen_option_from_transcript(transcript=transcript, options=["yes", "no", "new figure"])
    if choice:
        return choice
    else:
        message = "Didn't get your answer... let's play another round!"
        print(message)
        text_to_speech(message)
        return "yes"
