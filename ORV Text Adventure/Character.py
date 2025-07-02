import Stats as stats
import Item as item

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
        self.inventory = {}

    def displayLine(self):
        print("__________________________________________________________________________________")

    def displayAttributesWindow(self):
        self.displayLine()
        print("[Personal Information]")
        print("Name: " + self.name)
        print("Age: " + self.age)
        print("Sponsor: " + self.sponsor)
        print("Exclusive Attributes: " + str(self.attributes))
        print("Exclusive Skills: " + str(self.skills))
        print("Overall Stats: " + str(self.overallStats))
        self.displayLine()

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

    def deleteFromInventory(self, item):
        self.inventory.pop(item)

    def checkDeleteFromInventory(self, item):
        if self.inventory[item] == 0:
            self.deleteFromInventory(item)
    
    def addToInventory(self, item, quantity):
        for i in range(quantity):
            if item in self.inventory:
                self.inventory[item] = self.inventory[item] + 1
            else:
                self.inventory[item] = 1

    def removeFromInventory(self, item, quantity):
        for i in range(quantity):
            if item in self.inventory:
                self.inventory[item] = self.inventory[item] - 1
                self.checkDeleteFromInventory(item)
            else:
                print("ERROR: Attempted to remove item that doesn't exist in inventory")
                return

    def displayInventory(self):
        self.displayLine()
        print("[Inventory]")

        if len(self.inventory) == 0:
            print("Empty")
            return
        
        for item, quantity in self.inventory.items():
            print(f"{item.getName()} x{quantity}")
        self.displayLine()

class MainCharacter(Character):
    def __init__(self, name):
        super().__init__(name, "■")

# Character creation test
player = MainCharacter("Boo")
player.displayAttributesWindow()
# Inventory tests
something = item.Item("something")
somethingElse = item.Item("somethingElse")

player.displayInventory()
player.addToInventory(something, 1)
player.addToInventory(somethingElse, 9)
player.displayInventory()
player.removeFromInventory(somethingElse, 1)
player.removeFromInventory(something, 2)
player.displayInventory()
player.removeFromInventory(somethingElse, -1)
player.removeFromInventory(item.Item("aThing"), 1)
player.displayInventory()
