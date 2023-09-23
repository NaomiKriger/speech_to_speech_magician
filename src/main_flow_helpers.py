from src.commons import get_system_instructions, figures
from src.handle_audio import record_audio
from src.handle_transcript import text_to_speech, get_transcript, make_openai_request

welcome_prompt = "Hello! Welcome to the speech-to-speech wizard! Good to see you here.\n" \
                 "Whenever you'll be asked to talk - press and hold an arrow key while talking."


def start():
    print(f"\n\n{welcome_prompt}")
    text_to_speech(welcome_prompt)


def choose_figure():
    message = "Who do you want to talk to? Say the figure's name you want."
    print(f"\n\n{message}")
    text_to_speech(message)

    figure_options = list(figures.keys())
    for _, option in enumerate(figure_options, start=1):
        print(f"{option}")

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


async def play_round(user_choice: str):
    user_question_path = record_audio(file_name="user_question")
    transcription = await get_transcript(audio_file_path=user_question_path)
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
