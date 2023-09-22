from io import BytesIO
import pygame

from src.handle_transcript import make_openai_request


# def get_open_ai_respond():
#     text_respone_json = make_openai_request()
#     return text_respone_json
#
    # mp3_fp = BytesIO()

def main():
    # Read text from a file
    # file_path = 'your_text_file.txt'
    # with open(file_path, 'r', encoding='utf-8') as file:
    #     text = file.read()

    # Convert text to speech using gTTS
    speech = gTTS("everything isn't working", lang='en', lang_check=False, slow=False)

    # Play the speech using BytesIO and pygame
    speech_bytes = BytesIO()
    speech.write_to_fp(speech_bytes)
    speech_bytes.seek(0)

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(speech_bytes)
    pygame.mixer.music.play()

    # Wait for the speech to finish playing
    while pygame.mixer.music.get_busy():
        continue

if __name__ == "__main__":
   main()
