from enum import Enum

constant_instruction = "You provide funny and short answers."


def get_system_instructions(figure: str) -> str:
    return constant_instruction + f" You are: {figure}"


class Gender(Enum):
    female = "female"
    male = "male"


primary_figures = {"Marge Simpson": Gender.female.value,
                   "drunk fortune teller": Gender.female.value,
                   "Master Yoda": Gender.male.value,
                   "The Donkey from Shrek": Gender.male.value,
                   "Steve Jobs": Gender.male.value,
                   "Dobby the House Elf": Gender.male.value,
                   "Elsa the snow queen": Gender.female.value}

fallback_figures = {"Homer Simpson": Gender.male.value, "Hagrid": Gender.male.value,
                    "Hermione Granger": Gender.female.value, "Fiona": Gender.female.value,
                    "Pikachu": Gender.male.value, "Alice in Wonderland": Gender.female.value,
                    "SpongeBob SquarePants": Gender.male.value, "Shrek": Gender.male.value}
