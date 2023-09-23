import asyncio

from src.handle_transcript import text_to_speech
from src.main_flow_helpers import choose_figure, start, play_round, is_another_round

audio_sample_path = None


async def main():
    start()
    another_round = True
    chosen_figure = ""
    while True:
        if not chosen_figure:
            chosen_figure = await choose_figure()

        if chosen_figure == "no":
            farewell_message = "It was great having you here, hope to see you again soon!"
            print(f"\n{farewell_message}")
            text_to_speech(farewell_message)
            break
        elif chosen_figure == "new":
            chosen_figure = ""
            continue

        if not another_round:
            break

        while another_round:
            await play_round(chosen_figure=chosen_figure)
            chosen_figure = await is_another_round()
            if chosen_figure in ["yes"]:
                chosen_figure = ""
                break
            elif chosen_figure == "no":
                another_round = False
                break


if __name__ == "__main__":
    asyncio.run(main())
