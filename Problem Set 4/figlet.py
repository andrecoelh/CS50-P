from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")

    figlet.setFont(font=sys.argv[2])

else:
    sys.exit("Invalid usage")

texto = input("Input: ")
print(figlet.renderText(texto))