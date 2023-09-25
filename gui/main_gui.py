from pyfiglet import Figlet


def create_title(title):
    font_color_red = "\033[31m"
    font_color_reset = "\033[0m"

    f = Figlet(font='slant', width=140)
    rendered_text = (f.renderText(title))

    print(font_color_red, rendered_text, font_color_reset)
