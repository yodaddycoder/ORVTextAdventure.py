import random as rand
from character import Character as char, Inventory as inv, Stats as stats

LiamRyder = char.Character("Liam Ryder", 26)

OliviaBaker = char.Character("Olivia Baker", 37)

SamDavis = char.Character("Sam Davis", 15)

randomPersonList = [LiamRyder, OliviaBaker, SamDavis]

def randomPersonRandomizer():
    global randomPersonList
    rand.shuffle(randomPersonList)
    
