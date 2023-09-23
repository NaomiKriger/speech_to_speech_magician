from fuzzywuzzy import fuzz

from src.commons import get_system_instructions, figures
from src.handle_audio import record_audio
from src.handle_transcript import text_to_speech, get_transcript, make_openai_request

welcome_prompt = "Hello! Welcome to the speech-to-speech wizard! Good to see you here.\n" \
                 "Whenever you'll be asked to talk - press and hold an arrow key while talking."


def start():
    print(f"\n\n{welcome_prompt}")
    text_to_speech(welcome_prompt)


def get_figure_by_typing_input(figure_options: list) -> str:
    while True:
        choice = input("\nEnter the number of your chosen figure: ")
        try:
            if choice.lower() == "exit":
                return "exit"
            elif choice.lower() == "new":
                return "new"

            choice = int(choice)
            if 1 <= choice <= len(figure_options):
                chosen_figure = figure_options[choice - 1]
                print(f"You have chosen: {chosen_figure}")
                text_to_speech(f"You have chosen: {chosen_figure}")
                return chosen_figure
            else:
                print("Invalid choice. Please select a valid figure.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def detect_figure_from_transcript(transcript: str, figures_names: list) -> str:
    best_match_score = 0
    best_match = ""

    for figure_name in figures_names:
        score = fuzz.partial_ratio(transcript.lower(), figure_name.lower())
        if score > best_match_score:
            best_match_score = score
            best_match = figure_name

    if best_match_score >= 80:
        return best_match
    else:
        return ""


def update_figure_if_needed(figure: str) -> str:
    if not figure:
        figure = "Homer Simpson"
        message = "Ohhh too bad... seems you said something that isn't on or list...\n" \
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
    figure = detect_figure_from_transcript(transcript=transcript, figures_names=figures_names)
    figure = update_figure_if_needed(figure)

    return figure


async def choose_figure():
    message = "Who do you want to talk to? Say the figure's name you want."
    print(f"\n\n{message}")
    text_to_speech(message)

    figure_options = list(figures.keys())
    for _, option in enumerate(figure_options, start=1):
        print(f"{option}")

    figure = await get_figure_from_recording(figure_options)
    return figure


def ask_a_question(file_name: str) -> str:
    message = "Press + hold an arrow key to start talking to your chosen figure"
    print(message)
    text_to_speech(message)

    user_question_path = record_audio(file_name=file_name)
    return user_question_path


async def play_round(user_choice: str):
    user_question_path = ask_a_question(file_name="user_question")
    transcription = await get_transcript(audio_file_path=user_question_path,
                                         text_to_draw_while_waiting="Loading response")
    system_instructions = get_system_instructions(user_choice)
    gpt_answer = make_openai_request(
        system_instructions=system_instructions, user_question=transcription).choices[0].message["content"]
    print(gpt_answer)
    text_to_speech(gpt_answer, figures.get(user_choice))


def is_another_round() -> str:
    print("Do you want to play another round?")
    text_to_speech("Do you want to play another round? Type 'yes' or 'no'")
    choice = input("Type 'yes' or 'no': ")

    while True:
        try:
            if choice.lower() in ["new", "yes", "no"]:
                return choice.lower()
            else:
                print("No valid option was chosen. Please try again")
                choice = input("Do you want to play another round? \n"
                               "Type 'yes' or 'no'")
        except Exception as e:
            print(e)


def finish():
    print("Finishing the current session.")
