class Stat:
    def __init__(self, name):
        self.name = name
        self.exp = 0
        self.level = 0
        
    def __str__(self):
        return self.name + " Lv. " + str(self.level)
    
class StatsGroup:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        
    def __str__(self):
        if len(self.stats) == 0:
            return "None"

        display = ""
        for i in range(len(self.stats)):
            display += str(self.stats[i])
            if i == len(self.stats) - 1:
                display += "."
                break
            display += ", "
            
        return display

    def addStat(self, stat):
        self.stats.append(stat)

class Character:
    def __init__(self, name):
        self.name = name
        self.sponsor = "None"
        self.attributes = StatsGroup("Attributes", [])
        self.skills = StatsGroup("Skills", [])
        self.overallStats = StatsGroup("Overall Stats", [Stat("Stamina"), Stat("Strength"), Stat("Agility"), Stat("Mana")])
        self.health = 100

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

player = Character("Boo")
player.displayAttributesWindow()