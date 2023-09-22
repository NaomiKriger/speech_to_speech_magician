constant_instruction = "You provide funny answers."


def get_system_instructions(figure: str) -> str:
    return constant_instruction + f" You are: {figure}"
