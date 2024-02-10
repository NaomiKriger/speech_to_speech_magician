import asyncio

from src.handle_transcript import text_to_speech
from src.main_flow_helpers import choose_figure, start, play_round, is_another_round

audio_sample_path = None


def farewell() -> None:
    farewell_message = "It was great having you here, hope to see you again soon!"
    print(f"\n{farewell_message}")
    text_to_speech(farewell_message)


async def get_user_choices(figure: str) -> dict:
    another_round_user_choice = await is_another_round()
    if another_round_user_choice == "new figure":
        return {"figure": "", "another_round_user_choice": True}
    elif another_round_user_choice == "no":
        return {"figure": "", "another_round_user_choice": False}
    elif another_round_user_choice == "yes":
        return {"figure": figure, "another_round_user_choice": True}


async def main():
    start()
    another_round = True
    figure = ""

    while True:
        if not figure:
            figure = await choose_figure()

        while another_round:
            await play_round(chosen_figure=figure)
            user_choices = await get_user_choices(figure)
            figure, another_round = user_choices.get("figure"), user_choices.get("another_round_user_choice")
            if not figure:
                break

        if another_round is False:
            farewell()
            break


if __name__ == "__main__":
    asyncio.run(main())
