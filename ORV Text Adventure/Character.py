import Stats as stats

class Character:
    def __init__(self, name):
        self.name = name
        self.sponsor = "None"
        self.attributes = stats.StatsGroup("Attributes", [])
        self.skills = stats.StatsGroup("Skills", [])
        self.overallStats = stats.StatsGroup("Overall Stats", [stats.Stat("Stamina"), stats.Stat("Strength"), stats.Stat("Agility"), stats.Stat("Mana")])
        self.health = 100
        self.coins = 0

    def displayLine(self):
        print("__________________________________________________________________________________")

    def displayAttributesWindow(self):
        self.displayLine()
        print("[Personal Information]")
        print("Name: " + self.name)
        print("Age: ■")
        print("Sponsor: " + self.sponsor)
        print("Exclusive Attributes: " + str(self.attributes))
        print("Exclusive Skills: " + str(self.skills))
        print("Overall Stats: " + str(self.overallStats))
        self.displayLine()

    def displayHealth(self):
        print("[ You have a total of " + str(self.health) + " health points. ]")

    def addHealth(self, hp):
        self.health += hp
    
    def subtractHealth(self, hp):
        self.health -= hp

    def isAlive(self):
        if (self.health <= 0):
            return False
        return True

    def displayCoins(self):
        print("[ You have a total of " + str(self.coins) + " coins. ]")

    def addCoins(self, coins):
        self.coins += coins
    
    def subtractCoins(self, coins):
        self.coins -= coins

# player = Character("Boo")
# player.displayAttributesWindow()