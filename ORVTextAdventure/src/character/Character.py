from character.Stats import StatsGroup, Stat, Attribute, Grade as statGrade
from character.Inventory import Inventory
from helper import Text as text
import random

class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sponsor = "None"
        self.attributes = StatsGroup("Attributes", [])
        self.skills = StatsGroup("Skills", [])
        self.stigmas = StatsGroup("Stigmas", [])
        self.overallStats = StatsGroup("Overall Stats", [Stat("Stamina"), Stat("Strength"), Stat("Agility"), Stat("Mana")])
        self.health = 100
        self.coins = 0
        self.inventory = Inventory()
    
    ### ATTRIBUTE METHODS

    def addAttributes(self, *attributes):
        for attribute in attributes:
            self.attributes.addStat(attribute)

    def removeAttribute(self, attributeName):
        self.attributes.removeStat(attributeName)

    def displayAttributesWindow(self):
        text.displayLine()
        print("[Personal Information]")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Sponsor: {self.sponsor}")
        print(f"Exclusive Attributes: {self.attributes}")
        print(f"Exclusive Skills: {self.skills}")
        print(f"Stigma: {self.stigmas}")
        print(f"Overall Stats: {self.overallStats}")
        text.displayLine()

    def setName(self, name):
        self.name = name

    ### HEALTH METHODS

    def addHealth(self, hp):
        self.health += hp
    
    def subtractHealth(self, hp):
        self.health -= hp

    def setHealth(self, hp):
        self.health = hp

    def isAlive(self):
        if (self.health <= 0):
            return False
        return True

    ### COIN METHODS

    def addCoins(self, coins):
        self.coins += coins
    
    def subtractCoins(self, coins):
        self.coins -= coins
    
    def setCoins(self, coins):
        self.coins = coins

    ### INVENTORY METHODS

    def useEquipped(self):
        equipped = self.inventory.equipped
        if (equipped == None):
            self.inventory.showEquipped()
            return
        equipped.activateAbility()
        if equipped.consumable == True:
            print(f"Used up {equipped.name}")
            self.inventory.deleteEquipped()

    ### STAT METHODS

    def upgradeStat(self, stat, levels):
        if (stat.name == "undefined"):
            print("ERROR: Attempted to upgrade nonexistent stat")
            return
        upgradeCost = stat.upgrade(levels, self.coins)
        if (upgradeCost == 0):
            return
        self.coins -= upgradeCost

    def upgradeSkill(self, name, levels):
        stat = self.skills.getStat(name)
        self.upgradeStat(stat, levels)

    def upgradeStigma(self, name, levels):
        stat = self.stigmas.getStat(name)
        self.upgradeStat(stat, levels)

    def upgradeOverallStat(self, name, levels):
        stat = self.overallStats.getStat(name)
        self.upgradeStat(stat, levels)

    ### SKILL METHODS

    def addSkill(self, skill):
        self.skills.addStat(skill)

    def removeSkill(self, skillName):
        self.skills.removeStat(skillName)
    
    def activateSkill(self, skillName):
        skill = self.skills.getStat(skillName)
        if (skill.name == "undefined"):
            print("ERROR: Attempted to activate a skill that does not exist")
            print(f"[The exclusive skill {skill} has been activated.]")
            return
        skill.activate()

    ### STIGMA METHODS

    def addStigma(self, stigma):
        self.stigmas.addStat(stigma)

    def removeStigma(self, stigmaName):
        self.stigmas.removeStat(stigmaName)

    def activateStigma(self, stigmaName):
        stigma = self.stigmas.getStat(stigmaName)
        if (stigma.name == "undefined"):
            print("ERROR: Attempted to activate a stigma that does not exist")
            print(f"[The stigma {stigma} has been activated.]")
            return
        stigma.activate()
        
class MainCharacter(Character):
    def __init__(self, name):
        super().__init__(name, "■")

    def addName(self):
        print("You open your attributes window.")
        print("A blue screen appears again before you with your name at the very top.")
        inputName = ""
        while inputName == "":
            inputName = input("That name is ")
        self.name = inputName

    def displayAttributesWindow(self):
        if self.name == "":
            self.addName()
        return super().displayAttributesWindow()
    
    def displayHealth(self):
        print(f"[You have a total of {str(self.health)} health points.]")
        
    def addCoins(self, coins):
        print(f"[{coins} coins have been acquired.]")

    def displayCoins(self):
        print(f"[You have a total of {str(self.coins)} coins.]")

    # [The item '__' has been acquired.]

    def addSkill(self, skill):
        super().addSkill(skill)
        print(f"[The exclusive skill \'{skill.name}\' has been acquired.]")

    def addStigma(self, stigma):
        super().addStigma(stigma)
        print(f"[The stigma \'{stigma.name}\' has been acquired.]")

class Enemy(Character):
    def __init__(self, name, health, attacks):
        super().__init__(name, "■")
        self.attacks = attacks
        self.setHealth(health)
    
    def randomEnemyAttack(self):
        return random.choice(self.attacks)

mc = MainCharacter("")