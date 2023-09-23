from src.commons import get_system_instructions
from src.handle_audio import record_audio
from src.handle_transcript import text_to_speech, get_transcript, make_openai_request

exit_option = "You can finish the game at any time. \n" \
              "Write 'new' to start a new game, write 'exit' to finish"


def start():
    print("\n\n"
          "Hello! Welcome to the speech-to-speech wizard! Good to see you here =)\n"
          f"{exit_option}")
    text_to_speech("Hello! Welcome to the speech-to-speech wizard! Good to see you here")


def choose_figure():
    print("\n\nChoose a figure from the list:")
    text_to_speech("Choose a figure from the list:")

    figure_options = ["Jewish mama", "drunk fortune teller", "Master Yoda",
                      "Donald Trump", "my future self", "Steve Jobs", "Elon Musk", "Oprah Winfrey"]
    for idx, option in enumerate(figure_options, start=1):
        print(f"{idx}. {option}")

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
    text_to_speech(gpt_answer)


def is_another_round() -> str:
    text_to_speech("Do you want to play another round? Type yes or no")
    choice = input("\nDo you want to play another round? \n"
                   f"Type 'yes' or 'no'. {exit_option}")

    while True:
        try:
            if choice.lower() in ["exit", "new", "yes", "no"]:
                return choice.lower()
            else:
                print("No valid option was chosen. Please try again")
                choice = input("Do you want to play another round? \n"
                               "Type 'yes' or 'no'")
        except Exception as e:
            print(e)


def finish():
    print("Finishing the current session.")
