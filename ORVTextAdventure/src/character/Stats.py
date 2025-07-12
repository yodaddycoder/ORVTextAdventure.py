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
        self.level = 0
        
    def __str__(self):
        return f"{self.name} Lv. {str(self.level)}"
    
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