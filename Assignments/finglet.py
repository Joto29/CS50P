import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

s = input("Input: ")

# no arguments → random font
if len(sys.argv) == 1:

    fonts = figlet.getFonts()
    font = random.choice(fonts)
    figlet.setFont(font=font)

    print(figlet.renderText(s))


# with -f or --font
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:

    font = sys.argv[2]
    figlet.setFont(font=font)

    print(figlet.renderText(s))


# invalid usage
else:
    sys.exit("Invalid usage")
        


    








