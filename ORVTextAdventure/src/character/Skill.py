from character.Stats import Stat

class Skill(Stat):
    def __init__(self, name, ability):
        super().__init__(name)
        self.ability = ability

    def __str__(self):
        if self.levelAdjustment == 0:
            return f"\'{self.name}\' Lv. {str(self.level)}"
        if (self.levelAdjustment) < 0:
            return f"\'{self.name}\' Lv. {str(self.getActiveLevel())} (-{abs(self.levelAdjustment)})"
        return f"\'{self.name}\' Lv. {str(self.getActiveLevel())} (+{self.levelAdjustment})"
    
    def getLevelExpRequirement(self, level):
        return super().getLevelExpRequirement(level) * 10
    
    def getUpgradeCost(self):
        return super().getUpgradeCost() * 100

    def activate(self):
        self.ability()