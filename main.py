from src.main_flow_helpers import choose_figure, start, play_round, is_another_round, record_audio

audio_sample_path = None


def main():
    start()
    another_round = True
    user_choice = ""
    global audio_sample_path

    if audio_sample_path is None:
        duration = 5
        print("Let's record an audio sample of yours. Press any key to start your recording. "
              f"\nYou will have {duration} seconds to record once you press a key")
        input("\nPress any key to start recording")

        # TODO: increase duration to 10 seconds
        audio_sample_path = record_audio(duration=duration, file_name="sample_for_training")
        print(audio_sample_path)

    while True:
        if not user_choice:
            user_choice = choose_figure()

        if user_choice in ["exit", "no"]:
            print("\nFinishing. Was great having you here, hope to see you again soon!")
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
