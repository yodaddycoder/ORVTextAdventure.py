from enum import Enum

class Grade(Enum):
    common = "Common"
    uncommon = "Uncommon"
    rare = "Rare"
    legendary = "Legendary"
    mythical = "Mythical"

class Stat:
    def __init__(self, name):
        self.name = name
        self.exp = 0
        self.level = 1
        self.levelAdjustment = 0
        
    def __str__(self):
        if self.levelAdjustment == 0:
            return f"{self.name} Lv. {str(self.level)}"
        if (self.levelAdjustment) < 0:
            return f"{self.name} Lv. {str(self.getActiveLevel())} (-{abs(self.levelAdjustment)})"
        return f"{self.name} Lv. {str(self.getActiveLevel())} (+{self.levelAdjustment})"
        
    
    ### LEVEL METHODS

    def getNextLevelExpRequirement(self):
        return (self.level + 1) * 10 - 10

    def checkUpgradeLevel(self):
        while self.exp >= self.getNextLevelExpRequirement():
            self.level += 1

    def addExp(self, exp):
        self.exp += exp
        self.checkUpgradeLevel()
    
    def upgrade(self, levels, coins):
        totalUpgradeCost = 0
        for i in range(levels):
            if coins < self.getUpgradeCost():
                print(f"Failed to upgrade {self.name} to level {self.level + 1} due to insufficient coins")
                return 0
            totalUpgradeCost += self.getUpgradeCost()
            self.addExp(self.getNextLevelExpRequirement() - self.exp)
            print(f"Successfully upgraded {self.name} to level {self.level}")
        return totalUpgradeCost

    def getUpgradeCost(self):
        expNeeded = self.getNextLevelExpRequirement() - self.exp
        return expNeeded * 10 * self.level
    
    # LEVEL ADJUSTMENTS

    def addLevelAdjustment(self, adjustment):
        self.levelAdjustment += adjustment
    
    def setLevelAdjustment(self, adjustment):
        self.levelAdjustment = adjustment

    def getActiveLevel(self):
        if self.level + self.levelAdjustment < 0:
            return 1
        return self.level + self.levelAdjustment

class Attribute:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} ({self.grade.value})"
    
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
            if i != len(self.stats) - 1:
                display += ", "
            
        return display

    def addStat(self, stat):
        self.stats.append(stat)

    def removeStat(self, statName):
        for stat in self.stats:
            if (stat.name == statName):
                self.stats.remove(stat)
        print("ERROR: Attempted to remove a stat that does not exist")

    def getStat(self, statName):
        for stat in self.stats:
            if (stat.name == statName):
                return stat
        print("ERROR: Attempted to access a stat that does not exist")
        return Stat("undefined")