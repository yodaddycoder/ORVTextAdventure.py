import sys, time, os

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


# Notes from novel
# The item '___' has been acquired
# [Personal skill, ____, activated]