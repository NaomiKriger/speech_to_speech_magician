from src.handle_audio import get_audio_sample
from src.handle_transcript import text_to_speech
from src.main_flow_helpers import choose_figure, start, play_round, is_another_round

audio_sample_path = None


def main():
    start()
    another_round = True
    user_choice = ""
    global audio_sample_path

    if audio_sample_path is None:
        audio_sample_path = get_audio_sample()

    while True:
        if not user_choice:
            user_choice = choose_figure()

        if user_choice in ["exit", "no"]:
            print("\nFinishing. Was great having you here, hope to see you again soon!")
            text_to_speech("Finishing. Was great having you here, hope to see you again soon!")
            break
        elif user_choice == "new":
            user_choice = ""
            continue

        if not another_round:
            break

        while another_round:
            play_round(user_choice=user_choice)
            user_choice = is_another_round()
            if user_choice == "new":
                user_choice = ""
                break
            elif user_choice in ["exit", "no"]:
                another_round = False
                break


if __name__ == "__main__":
    main()
