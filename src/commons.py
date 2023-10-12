from enum import Enum


def get_system_instructions(figure: str) -> str:
    return f"You provide funny and short answers. You are: {figure}"


class Gender(Enum):
    FEMALE = "female"
    MALE = "male"


primary_figures = {"Marge Simpson": Gender.FEMALE.value,
                   "drunk fortune teller": Gender.FEMALE.value,
                   "Master Yoda": Gender.MALE.value,
                   "The Donkey from Shrek": Gender.MALE.value,
                   "Steve Jobs": Gender.MALE.value,
                   "Dobby the House Elf": Gender.MALE.value,
                   "Elsa the snow queen": Gender.FEMALE.value}

fallback_figures = {"Homer Simpson": Gender.MALE.value, "Hagrid": Gender.MALE.value,
                    "Hermione Granger": Gender.FEMALE.value, "Fiona": Gender.FEMALE.value,
                    "Pikachu": Gender.MALE.value, "Alice in Wonderland": Gender.FEMALE.value,
                    "SpongeBob SquarePants": Gender.MALE.value, "Shrek": Gender.MALE.value}

WORDS_PER_MINUTE_RATE = 180
