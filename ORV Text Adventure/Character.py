import Stats as stats
import Inventory as inv
import Text as text

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

    def displayAttributesWindow(self):
        text.displayLine()
        print("[Personal Information]")
        print("Name: " + self.name)
        print("Age: " + self.age)
        print("Sponsor: " + self.sponsor)
        print("Exclusive Attributes: " + str(self.attributes))
        print("Exclusive Skills: " + str(self.skills))
        print("Overall Stats: " + str(self.overallStats))
        text.displayLine()

    def displayHealth(self):
        print("[You have a total of " + str(self.health) + " health points.]")

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

    def displayCoins(self):
        print("[You have a total of " + str(self.coins) + " coins.]")

    def addCoins(self, coins):
        self.coins += coins
    
    def subtractCoins(self, coins):
        self.coins -= coins
    
    def setCoins(self, coins):
        self.coins = coins

class MainCharacter(Character):
    def __init__(self, name):
        super().__init__(name, "■")