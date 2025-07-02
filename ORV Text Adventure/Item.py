from enum import Enum

class Grade(Enum):
    A = "A"

class Item:
    def __init__(self, name, consumable, grade, ability):
        self.name = name
        self.consumable = consumable
        self.grade = grade
        self.ability = ability

    def getName(self):
        return self.name
    
    def isConsumable(self):
        return self.consumable
    
    def activateAbility(self):
        self.ability()