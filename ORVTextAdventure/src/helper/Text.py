import sys, time, os
from enum import Enum

class Color(Enum):
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    ORANGE = "\033[38;5;166m"

class Modifier(Enum):
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    RESET = "\033[0m"

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    sys.stdout.write("\n")

def displayLine():
    print("__________________________________________________________________________________")

def modifyText(modifier, text):
    return f"{modifier.value}{text}{Modifier.RESET.value}"

# Notes from novel
# The item '___' has been acquired
# [Personal skill, ____, activated]