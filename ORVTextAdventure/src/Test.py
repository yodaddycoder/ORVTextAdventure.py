from character.Character import Character, MainCharacter, Enemy
from character.Stats import Attribute, Grade as statGrade
from character.Item import Item, Grade as itemGrade
from character.Skill import Skill
from character.Stigma import Stigma
from helper import Text as text
from story import Prologue as prologue
import Constellations as cons

### Character creation test
player = MainCharacter("Boo")

### Stigma tests
# player.displayAttributesWindow()
# def basicStigma():
#     print("A basic Stigma")

# basicStigma = Stigma("Basic Stigma", basicStigma)
# player.addStigma(basicStigma)
# player.displayAttributesWindow()
# player.setCoins(100000)
# player.upgradeStigma("Basic Stigma", 1)
# player.stigmas.getStat("Basic Stigma").addExp(100)
# player.displayAttributesWindow()
# player.activateStigma("Basic Stigma")
# player.removeStigma("Basic Stigma")
# player.removeStigma("Basic Stigma")
# player.activateStigma("Basic Stigma")
# player.activateStigma("Nonexistent Stigma")
# player.displayAttributesWindow()

### Skill tests
# def basicSkill():
#     print("A basic skill")

# basicSkill = Skill("Basic Skill", basicSkill)
# player.addSkill(basicSkill)
# player.displayAttributesWindow()
# player.setCoins(100000)
# player.upgradeSkill("Basic Skill", 1)
# player.skills.getStat("Basic Skill").addExp(100)
# player.displayAttributesWindow()
# player.activateSkill("Basic Skill")
# player.removeSkill("Basic Skill")
# player.removeSkill("Basic Skill")
# player.activateSkill("Basic Skill")
# player.activateSkill("Nonexistent Skill")
# player.displayAttributesWindow()

### Attribute tests
# player.displayAttributesWindow()
# player.addAttributes(Attribute("Kitty", statGrade.common)) # test adding one attribute
# player.displayAttributesWindow()
# player.addAttributes(Attribute("Cute", statGrade.rare), Attribute("Big Brain", statGrade.legendary)) # test adding multiple attributes
# player.addAttributes() # test adding no attributes
# player.displayAttributesWindow()
# player.removeAttribute("Big Brain") # test removing attribute
# player.displayAttributesWindow()
# player.removeAttribute("Fake Attribute") # test removing fake attribute
# player.displayAttributesWindow()

### Stat tests
# print(player.overallStats.getStat("Stamina").name) # test getting stats
# print(player.overallStats.getStat("Nonexistent stat").name) # test getting nonexistent stats

# player.upgradeOverallStat("Nonexistent stat", 1)
# player.upgradeOverallStat("Stamina", 1)
# player.setCoins(1000000)
# player.upgradeOverallStat("Stamina", 1)
# player.displayAttributesWindow()
# player.displayCoins()
# player.upgradeOverallStat("Stamina", 3)
# player.displayAttributesWindow()
# player.displayCoins()
# print(f"Exp required for next Stamina level: {player.overallStats.getStat('Stamina').getNextLevelExpRequirement()}")
# print(f"Coins required for next Stamina level: {player.overallStats.getStat('Stamina').getUpgradeCost()}")
# player.overallStats.getStat("Stamina").addExp(3)
# print(f"Coins required for next Stamina level: {player.overallStats.getStat('Stamina').getUpgradeCost()}")
# player.upgradeOverallStat("Stamina", 1)
# print(f"Coins required for next Stamina level: {player.overallStats.getStat('Stamina').getUpgradeCost()}")
# player.overallStats.getStat("Stamina").addExp(10)
# player.displayCoins()
# player.displayAttributesWindow()

# player.overallStats.getStat("Stamina").addLevelAdjustment(1)
# player.displayAttributesWindow()
# player.overallStats.getStat("Stamina").addLevelAdjustment(-1)
# player.displayAttributesWindow()
# player.overallStats.getStat("Stamina").addLevelAdjustment(-3)
# player.displayAttributesWindow()

# player.overallStats.getStat("Stamina").setLevel(5)
# print(f"Stamina EXP: {player.overallStats.getStat('Stamina').exp}")
# player.overallStats.getStat("Stamina").addLevelAdjustment(-3)
# player.displayAttributesWindow()

### Coin and health tests
# player.setCoins(10)
# player.displayCoins()
# player.addCoins(41)
# player.displayCoins()
# player.subtractCoins(2)
# player.displayCoins()
# player.subtractCoins(100)
# player.displayCoins()
# player.setHealth(10)
# player.displayHealth()
# player.addHealth(41)
# player.displayHealth()
# player.subtractHealth(2)
# player.displayHealth()
# player.subtractHealth(100)
# player.displayHealth()

### Inventory tests
# def basicAbility(): print(f"Used a basic ability!")
# something = Item("something", False, itemGrade.A, basicAbility)
# something.addDescription("This item was created for some reason idk.")
# something.addAbilityDescription("Wow this item does something.")

# somethingElse = Item("somethingElse", True, itemGrade.D, basicAbility)
# somethingElse.addDescription("This item was created for some reason idk.")
# somethingElse.addAbilityDescription("Wow this item does something. Oh btw it can only be used once.")

# aThing = Item("aThing", True, itemGrade.Constellation, basicAbility)

# player.inventory.displayInventory()
# player.inventory.addToInventory(something, 1)
# player.inventory.addToInventory(somethingElse, 9)
# player.inventory.displayInventory()
# player.inventory.removeFromInventory(somethingElse, 1)
# player.inventory.removeFromInventory(something, 2)
# player.inventory.displayInventory()
# player.inventory.removeFromInventory(somethingElse, -1)
# player.inventory.removeFromInventory(aThing, 1)
# player.inventory.addToInventory(something, 1)
# player.inventory.displayInventory()

### Equipped item tests
# player.useEquipped()
# player.inventory.accessInventory() # Equip somethingElse
# player.inventory.showEquipped()
# player.useEquipped()
# player.inventory.accessInventory() # Equip something
# player.inventory.showEquipped()
# player.useEquipped()
# player.inventory.displayInventory()

### Item info tests
# something.displayDetails()
# somethingElse.displayDetails()

### Inventory access tests
# player.inventory.accessInventory()

### Prologue test
# text.typingPrint("Testing typing print")
# text.typingPrint("Testing typing print again")
# print("Testing normal print")
# text.typingPrint("Testing typing print one last time")
# prologue.prologue()
# for i in range (10):
#     print("Constellation choices")
#     cons.randomConstellation()
#     print()

### Text effects test
# print(text.modifyText(text.Color.RED, "Red color test"))
# print(text.modifyText(text.Color.BLUE, "Blue color test"))
# print(text.modifyText(text.Color.CYAN, "Cyan color test"))
# print(text.modifyText(text.Color.GREEN, "Green color test"))
# print(text.modifyText(text.Color.ORANGE, "Orange color test"))
# print(text.modifyText(text.Color.PURPLE, "Purple color test"))
# print(text.modifyText(text.Color.YELLOW, "Yellow color test"))
# print(text.modifyText(text.Modifier.BLINK, "Blink modifier test"))
# print(text.modifyText(text.Modifier.BOLD, "Bold modifier test"))
# print(text.modifyText(text.Modifier.CROSSED, "Crossed modifier test"))
# print(text.modifyText(text.Modifier.FAINT, "Faint modifier test"))
# print(text.modifyText(text.Modifier.ITALIC, "Italic modifier test"))
# print(text.modifyText(text.Modifier.NEGATIVE, "Negative modifier test"))
# print(text.modifyText(text.Modifier.UNDERLINE, "Underline modifier test"))