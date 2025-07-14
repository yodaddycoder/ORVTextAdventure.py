from character.Skill import Skill

class Stigma(Skill):
    def __init__(self, name, ability):
        super().__init__(name, ability)

    def activate(self):
        self.ability()