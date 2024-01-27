from enum import Enum


def get_system_instructions(figure: str) -> str:
    return f"You provide funny and short answers. You are: {figure}"


class Gender(Enum):
    FEMALE = "female"
    MALE = "male"


gender = "gender"


primary_figures = {"Marge Simpson": {gender: Gender.FEMALE.value},
                   "drunk fortune teller": {gender: Gender.FEMALE.value},
                   "Master Yoda": {gender: Gender.MALE.value},
                   "The Donkey from Shrek": {gender: Gender.MALE.value},
                   "Steve Jobs": {gender: Gender.MALE.value},
                   "Dobby the House Elf": {gender: Gender.MALE.value},
                   "Elsa the snow queen": {gender: Gender.FEMALE.value}}

fallback_figures = {"Homer Simpson": {gender: Gender.MALE.value}, "Hagrid": {gender: Gender.MALE.value},
                    "Hermione Granger": {gender: Gender.FEMALE.value}, "Fiona": {gender: Gender.FEMALE.value},
                    "Pikachu": {gender: Gender.MALE.value}, "Alice in Wonderland": {gender: Gender.FEMALE.value},
                    "SpongeBob SquarePants": {gender: Gender.MALE.value}, "Shrek": Gender.MALE.value}

WORDS_PER_MINUTE_RATE = 180
