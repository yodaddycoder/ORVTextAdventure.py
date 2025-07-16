import random as rand

from character.Character import Character
from character.Inventory import Inventory

path = "ORVTextAdventure/src/character/names/"

firstNamesFile = open(path + "firstNames.txt", "rt")
lastNamesFile = open(path + "lastNames.txt", "rt")

firstNames = firstNamesFile.read().split(",")
lastNames = lastNamesFile.read().split(",")

randomPersonList = []

def createRandomPerson():
    global firstNames
    global lastNames
    randomFirstName = rand.choice(firstNames)
    randomLastName = rand.choice(lastNames)
    randomAge = rand.randint(13, 80)
    randomPerson = Character(f"{randomFirstName} {randomLastName}", randomAge)    
    return randomPerson

for i in range(0, 2):
    randomPersonList.append(createRandomPerson())

def randomPersonRandomizer():
    global randomPersonList
    rand.shuffle(randomPersonList)
    
    
# ideas: could randomize name combination and age