from enum import Enum

class Grade(Enum):
    Constellation = "Constellation"
    S = "S"
    A = "A"
    B = "B"
    C = "C"
    D = "D"

class Item:
    def __init__(self, name, consumable, grade, ability):
        self.name = name
        self.consumable = consumable
        self.grade = grade
        self.ability = ability
    
    def isConsumable(self):
        return self.consumable
    
    def activateAbility(self):
        self.ability()