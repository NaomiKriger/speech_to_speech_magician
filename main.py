import argparse

exit_option = "You can finish the game at any time. \n" \
              "Write 'new' to start a new game, write 'exit' to finish"


def start():
    print("\n\n")
    print("Hello! Welcome to the speech-to-speech wizard! Good to see you here =)")
    print(exit_option)


def choose_figure():
    print("\n\nChoose a figure from the list:")

    figure_options = ["Figure 1", "Figure 2", "Figure 3"]
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
                return chosen_figure
            else:
                print("Invalid choice. Please select a valid figure.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_audio_input():
    print(f"\nClick the record button and ask a question...")
    return "this is the user audio"
    # Implement your logic for asking questions here


def get_transcription(audio_input):
    return "some transcription"


def get_gpt_answer(transcription: str, figure: str) -> str:
    return "gpt_answer"


def play_gpt_response(transcript: str):
    return "playing response"


def is_another_round() -> str:
    choice = input("Do you want to play another round? \n"
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


def main():
    parser = argparse.ArgumentParser(description="Question Answering Tool")
    start()
    user_choice = choose_figure()

    if user_choice == "exit":
        print("Finishing. Was great having you here, hope to see you again soon!")

    elif user_choice == "new":
        main()

    else:
        another_round = True
        while another_round:
            audio_stream = get_audio_input()
            transcription = get_transcription(audio_input=audio_stream)
            gpt_answer = get_gpt_answer(transcription=transcription, figure=user_choice)
            play_gpt_response(gpt_answer)
            user_choice = is_another_round()
            if user_choice == "new":
                main()
            elif user_choice in ["exit", "no"]:
                print("Finishing. Was great having you here, hope to see you again soon!")
                another_round = False


if __name__ == "__main__":
    main()
