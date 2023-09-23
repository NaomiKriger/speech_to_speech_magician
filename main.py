import asyncio

from src.handle_transcript import text_to_speech
from src.main_flow_helpers import choose_figure, start, play_round, is_another_round

audio_sample_path = None


async def main():
    start()
    another_round = True
    figure = ""
    user_choice = ""

    while True:
        if not figure:
            figure = await choose_figure()

        if user_choice == "no":
            farewell_message = "It was great having you here, hope to see you again soon!"
            print(f"\n{farewell_message}")
            text_to_speech(farewell_message)
            break
        elif user_choice == "new figure":
            figure = ""
            user_choice = ""
            continue

        if not another_round:
            break

        while another_round:
            await play_round(chosen_figure=figure)
            user_choice = await is_another_round()
            if user_choice == "new figure":
                figure = ""
                user_choice = ""
                break
            elif user_choice == "no":
                another_round = False
                break
            elif user_choice == "yes":
                break


if __name__ == "__main__":
    asyncio.run(main())
