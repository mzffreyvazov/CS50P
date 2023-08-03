import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
try:
    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font = sys.argv[2]
        figlet.setFont(font=font)
        b = input("Input: ")
        print(figlet.renderText(b))
    elif len(sys.argv) == 1:
        figlet.setFont(font=random.choice((figlet.getFonts())))
        a = input("Input: ")
        print(figlet.renderText(a))
    else:
        sys.exit(1)
except:
    sys.exit("Invalid usage")



