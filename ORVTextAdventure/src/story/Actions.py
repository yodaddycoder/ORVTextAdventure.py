import time
from character.Character import Character, MainCharacter, mc

def blank():
    return

returnFunction = blank

def setReturnFunction(function):
    global returnFunction
    returnFunction = function

# Chooses an action from a list of options
def chooseAction(choices):
    userInput = ""
    while userInput not in choices.keys():
        print(f"Options: {(', ').join(choices.keys())}")
        userInput = input("")
        time.sleep(1)
        if userInput in choices.keys():
            choices[userInput]()
        else:
            print("Please enter a valid option for the game.")

def otherChoices():
    choices = {
        "view attributes window": mc.displayAttributesWindow,
        "return": blank
    }
    chooseAction(choices)
    returnFunction()