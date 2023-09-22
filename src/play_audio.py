import pygame


def play_audio(file_name: str = "recording.wav"):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.delay(100)

    pygame.quit()


# Example usage:
play_audio("recording.wav")
