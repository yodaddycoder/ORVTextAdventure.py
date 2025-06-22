import time
import random 

wait = time.sleep(1)

characterHealth = 100
violentPersonAlive = True
introSceneTrigger = False
constellationChosen = False

# All Classes
class Enemy:
    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
        self.attacks = attacks

class Constellation:
    def __init__(self, name, stigma):
        self.name = name
        self.stigma = stigma

# Chooses random attack
def randomAttack(self):
        return random.choice(self.attacks)

# Constellations and their stigmas
def steelLikeDefense():
    pass 
masterOfSteel = Constellation("Master of Steel", steelLikeDefense)

def songOfTheWater():
    pass
navalGeneral = Constellation("Naval General", songOfTheWater)

def abyssOfDarkness():
    pass
darkVoidedBird = Constellation("Dark Voided Bird", abyssOfDarkness)

def timeOfVerdict():
    pass
juryOfWater = Constellation("Jury of Water", timeOfVerdict)

def scheming():
    pass
deviousSchemer = Constellation("Devious Schemer", scheming)

def shineBrightLikeADiamond():
    pass
ablazingSun = Constellation("Ablazing Sun", shineBrightLikeADiamond)

def lesserBeing():
    pass
duskEffigy = Constellation("Dusk Effigy", lesserBeing)

def pinpoint():
    pass
goldenStickAndString = Constellation("Golden Stick and String", pinpoint)


# Chooses Constellation
def randomConstellation():
    pass

# Navigation around the map
def introScene():
    choices = ["left, right, forward, backward,"]
    randomConstellation() == ["" + " none"]
    constellationChoices = randomConstellation()
    global introSceneTrigger
    if introSceneTrigger == False:
        print("You are on a subway in the secondary car. A blue futuristic screen appears infront of you.")
        print("[Scenario 1:]")
        print("[Kill at least one living organism within 5 minutes.]")
        print("Failure to do so will result in extermination.")
    else:
        print("You are back where you started.")
    userInput = ""
    while userInput not in constellationChoices:
        print(constellationChoices)
        if userInput == "none":
            print("You have no constellation.")
        elif userInput == "":
            # choosable constellations
            pass
    while userInput not in choices:
        print("Options, left, right, forward, backward")
        if userInput == "left":
            time.sleep(1)
            violentPerson1()
        elif userInput == "right":
            time.sleep(1)
            emptySpace()
        elif userInput == "forward":
            time.sleep(1)
            randomPerson()
        elif userInput == "backward":
            time.sleep(1)
            moneySpot1()
        else:
            print("Please enter a valid option for the game.")
    introSceneTrigger = True

def violentPerson1():
    global violentPersonAlive
    choices = ["left, right, talk, fight"]
    violentPersonDeadChoices = ["left, right, loot"]
    if violentPersonAlive == False:
        userInput1 = ""
        while userInput1 not in violentPersonDeadChoices:
            print("Options: left, right, loot")
            if userInput1 == "left":
                time.sleep(1)
                randomPerson()
            elif userInput1 == "right":
                time.sleep(1)
                introScene()
            elif userInput1 == "loot":
                time.sleep(1)
                lootViolentPerson1()
            else:
                print("Please enter a valid option for the game.")
    else:
        print("You see a man that looks very violent.")
        userInput = ""
        while userInput not in choices:
            print("Options: left, right, talk, fight")
            if userInput == "left":
                time.sleep(1)
                print("The man infront of you grabs you. He raises his fists.")
            elif userInput == "right":
                time.sleep(1)
                print("The man infront of you grabs you. He raises his fists.")
            elif userInput == "talk":
                time.sleep(1)
                print("He doesn't listen to your words and readies his fists.")
            elif userInput == "fight":
                time.sleep(1)
                print("He readies his fists to fight you.")
                time.sleep(1)
                fightViolentPerson()
            else:
                print("Please enter a valid option for the game.")

        

def emptySpace():
    pass

def randomPerson():
    pass

def moneySpot1():
    pass



# Fighting
def fightViolentPerson():
    pass

def lootViolentPerson1():
    pass


