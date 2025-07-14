import random as rand
from character.Character import Character
from character.Inventory import Inventory

LiamRyder = Character("Liam Ryder", 26)

OliviaBaker = Character("Olivia Baker", 37)

SamDavis = Character("Sam Davis", 15)

randomPersonList = [LiamRyder, OliviaBaker, SamDavis]

def randomPersonRandomizer():
    global randomPersonList
    rand.shuffle(randomPersonList)
    
# ideas: could randomize name combination and age