from enum import Enum

constant_instruction = "You provide funny and short answers."


def get_system_instructions(figure: str) -> str:
    return constant_instruction + f" You are: {figure}"


class Gender(Enum):
    female = "female"
    male = "male"


figures = {"Jewish mama": Gender.female.value,
           "drunk fortune teller": Gender.female.value,
           "Master Yoda": Gender.male.value,
           "Donald Trump": Gender.male.value,
           "Steve Jobs": Gender.male.value,
           "Elon Musk": Gender.male.value,
           "Oprah Winfrey": Gender.female.value}
