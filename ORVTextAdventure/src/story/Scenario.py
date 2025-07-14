from enum import Enum
from helper import Text as text

class Difficulty(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"

class Scenario:
    def __init__(self, name, difficulty, clearConditions, timeLimit, compensation, penalty):
        self.name = name
        self.difficulty = difficulty
        self.clearConditions = clearConditions
        self.timeLimit = timeLimit
        self.compensation = compensation
        self.failure = penalty
        self.cleared = False

class SubScenario(Scenario):
    pass

class MainScenario(Scenario):
    def __init__(self, name, number, difficulty, clearConditions, timeLimit, compensation, penalty):
        super().__init__(name, difficulty, clearConditions, timeLimit, compensation, penalty)
        self.number = number
    
    def displayScenario(self):
        text.displayLine()
        print(f"[Main Scenario #{self.number} - {self.name}]")
        print(f"Category: Main")
        print(f"Difficulty: {self.difficulty.value}")
        print(f"Clear Conditions: {self.clearConditions}")
        print(f"Time Limit: {self.timeLimit}")
        print(f"Compensation: {self.compensation}")
        print(f"Failure: {self.failure}")
        text.displayLine()