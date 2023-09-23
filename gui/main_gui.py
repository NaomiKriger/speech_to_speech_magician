from pyfiglet import Figlet

font_color_red = "\033[31m"
font_color_reset = "\033[0m"

f = Figlet(font='slant', width=140)
renderd_text = (f.renderText('Speech to Speech wizard'))


print(font_color_red, renderd_text, font_color_reset)