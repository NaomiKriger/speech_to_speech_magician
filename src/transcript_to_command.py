from src.text_to_ai_integration import make_openai_request

user_input_1 = "What does Harry Potter like in Hogwarts?"
user_input_2 = "What makes everyone happy?"

constant_instruction = "You provide funny answers."


def get_figure_chosen_by_user():
    return "drunk future teller"


chosen_figure_by_user = get_figure_chosen_by_user()
request_based_instruction = f" You are: {chosen_figure_by_user}"


def get_user_question():
    return "What does Harry Potter like in Hogwarts?"


user_question = get_user_question()

res = make_openai_request(system_instruction=constant_instruction + request_based_instruction,
                          user_question=user_question)

print(res)
