import time
import random 
import Constellations as cons
from character import Talk as talk
from character import RandomPerson as rp
from character.Character import Character, MainCharacter, Enemy, mc
from story.Scenario import MainScenario, Difficulty
from story.Actions import *

characterHealth = 100
violentPersonAlive = True
introSceneTrigger = False
constellationChosen = False
randomPersonOneAlive = True
randomPersonTwoAlive = True
randomPersonThreeAlive = True
foundMoneySpot1 = False
foundMoneySpot2 = False


scenario = MainScenario("Prove Your Worth", 1, Difficulty.F, "Kill at least one living organism.", "5 minutes", "300 coins", "Extermination")

# Randomizes random persons
rp.randomPersonRandomizer()

# Navigation around the map
def introScene():
    choices = {
        "left": violentPerson1,
        "right": emptySpace,
        "forward": randomPerson,
        "backward": moneySpot1,
        "view attributes window": displayAttributesWindow
    }
    setReturnFunction(introScene)
    global introSceneTrigger
    if introSceneTrigger == False:
        print("You are on a subway in the secondary car. A blue futuristic screen appears infront of you.")
        time.sleep(1)
        print()
        scenario.displayScenario()
        time.sleep(1)
        print()
        introSceneTrigger = True
    else:
        print("You are back where you started.")
    chooseAction(choices)
    introSceneTrigger = True

def violentPerson1():
    global violentPersonAlive
    choices = ["left, right, talk, fight"]
    violentPersonDeadChoices = ["left, right, loot"]
    if violentPersonAlive == False:
        userInput1 = ""
        while userInput1 not in violentPersonDeadChoices:
            print("Options: left, right, loot")
            userInput1 = input("")
            time.sleep(1)
            if userInput1 == "left":
                randomPerson()
            elif userInput1 == "right":
                introScene()
            elif userInput1 == "loot":
                lootViolentPerson1()
            else:
                print("Please enter a valid option for the game.")
    else:
        print("You see a man that looks very violent.")
        userInput = ""
        while userInput not in choices:
            print("Options: left, right, talk, fight")
            userInput = input("")
            time.sleep(1)
            if userInput == "left":
                print("The man infront of you grabs you. He raises his fists.")
            elif userInput == "right":
                print("The man infront of you grabs you. He raises his fists.")
            elif userInput == "talk":
                print("He doesn't listen to your words and readies his fists.")
            elif userInput == "fight":
                print("He readies his fists to fight you.")
                time.sleep(1)
                fightViolentPerson()
            else:
                print("Please enter a valid option for the game.")

def emptySpace():
    print("You arrive at an empty space.")
    choices = {
        "left": introScene
    }
    setReturnFunction(emptySpace)
    chooseAction(choices)

def randomPerson():
    global randomPersonOneAlive
    if randomPersonOneAlive == True:
        print("Hello there, would you like to talk?")
        choices = {
            "backward": introScene,
            "talk": talk.conversation,
            "view attributes window": displayAttributesWindow
        }

def moneySpot1():
    global foundMoneySpot1
    if foundMoneySpot1 == False:
        print("You found money on the ground. Would you like to pick it up?")
        choices = ["forward, pick up money, view attributes window"]
        userInput = ""
        while userInput not in choices:
            print("Options: forward, pick up money, view attributes window")
            userInput = input("")
            if userInput == "forward":
                introScene()
            elif userInput == "pick up money":
                Character.addCoins(0, 50)
            elif userInput == "view attributes window":
                Character.displayAttributesWindow()
            else:
                print("Please enter a valid option for the game.")
        foundMoneySpot1 = True
    else:
        print("You are at an empty spot.")
        foundMoneyChoices = ["forward, view attributes window"]
        userInput = ""
        while userInput not in choices:
            print("Options: forward, view attributes window")
            userInput = input("")
            if userInput == "forward":
                introScene()
            elif userInput == "view attributes window":
                Character.displayAttributesWindow()
            else:
                print("Please enter a valid option for the game.")
        
        




# Fighting
def fightViolentPerson():
    pass

def lootViolentPerson1():
    pass
