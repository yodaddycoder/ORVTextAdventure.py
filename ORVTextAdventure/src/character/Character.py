from character import Stats as stats, Inventory as inv
from helper import Text as text
import random

class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sponsor = "None"
        self.attributes = stats.StatsGroup("Attributes", [])
        self.skills = stats.StatsGroup("Skills", [])
        self.overallStats = stats.StatsGroup("Overall Stats", [stats.Stat("Stamina"), stats.Stat("Strength"), stats.Stat("Agility"), stats.Stat("Mana")])
        self.health = 100
        self.coins = 0
        self.inventory = inv.Inventory()
    
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
        print(f"Exclusive Attributes: {str(self.attributes)}")
        print(f"Exclusive Skills: {str(self.skills)}")
        print(f"Overall Stats: {str(self.overallStats)}")
        text.displayLine()

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

class MainCharacter(Character):
    def __init__(self, name):
        super().__init__(name, "■")
    
    def displayHealth(self):
        print(f"[You have a total of {str(self.health)} health points.]")
        
    def displayCoins(self):
        print(f"[You have a total of {str(self.coins)} coins.]")

class Enemy(Character):
    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
        self.attacks = attacks
    
    def randomEnemyAttack(self):
        return random.choice(self.attacks)
