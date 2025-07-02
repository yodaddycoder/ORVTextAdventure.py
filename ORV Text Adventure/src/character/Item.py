from enum import Enum
import Text as text

class Grade(Enum):
    Constellation = "Constellation Artifact"
    SSS = "SSS"
    SS = "SS"
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
        self.description = "No description provided."
        self.abilityDescription = "No ability information provided."
    
    def isConsumable(self):
        return self.consumable
    
    def activateAbility(self):
        self.ability()
    
    def addDescription(self, description):
        self.description = description

    def addAbilityDescription(self, description):
        self.abilityDescription = description
    
    def displayDetails(self):
        text.displayLine()
        print("[Item Information]")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade.value}")
        print(f"Description: {self.description}")
        print(self.abilityDescription)
        text.displayLine()