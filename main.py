import asyncio

from src.handle_transcript import text_to_speech
from src.main_flow_helpers import choose_figure, start, play_round, is_another_round

audio_sample_path = None


async def main():
    start()
    another_round = True
    user_choice = ""
    while True:
        if not user_choice:
            user_choice = await choose_figure()

        if user_choice == "no":
            farewell_message = "It was great having you here, hope to see you again soon!"
            print(f"\n{farewell_message}")
            text_to_speech(farewell_message)
            break
        elif user_choice == "new":
            user_choice = ""
            continue

        if not another_round:
            break

        while another_round:
            await play_round(user_choice=user_choice)
            user_choice = is_another_round()
            if user_choice in ["new", "yes"]:
                user_choice = ""
                break
            elif user_choice == "no":
                another_round = False
                break


if __name__ == "__main__":
    asyncio.run(main())
