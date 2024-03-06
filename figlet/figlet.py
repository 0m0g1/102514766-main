import sys
import random
from pyfiglet import Figlet

figlet = Figlet()


def main():
    try:
        if len(sys.argv) == 0:
            figlet.setFont(font=random.choice(figlet.getFonts()))
        elif len(sys.argv) == 3:
            if sys.argv[1] in ["-f", "--font"]:
                figlet.setFont(font=sys.argv[2])
                print(figlet.renderText(input("Input: ").strip()))
                return 0
    except:
        pass
    sys.exit("Invalid command")

main()
