import time
from helper import Text as text

def prologue():
    text.clearScreen()
    text.typingPrint("There are three ways to survive in a ruined world.")
    time.sleep(1)
    text.typingPrint("Everything is fading and becoming unclear now. But one thing is certain.")
    time.sleep(1)
    text.typingPrint("If you're reading this, you will survive.")
    time.sleep(1)
    print()
    text.typingPrint("Inspired by Omniscient Reader's Viewpoint by singNsong")
    print()
    time.sleep(3)
    text.typingPrint("ORV Text Adventure")
    time.sleep(5)
    text.clearScreen()

def startGame():
    while True:
        start = input("Would you like to start reading? (y/n)\n")
        if start == "y" or start == "n":
            break

    if start == "y":
        return True
    else:
        return False