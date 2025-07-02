import Character as c
import Item as item

# Character creation test
player = c.MainCharacter("Boo")
player.displayAttributesWindow()
# Inventory tests
def basicAbility(): print(f"Used a basic ability!")
something = item.Item("something", False, item.Grade.A, basicAbility)
somethingElse = item.Item("somethingElse", True, item.Grade.A, basicAbility)
aThing = item.Item("aThing", True, item.Grade.A, basicAbility)

player.displayInventory()
player.addToInventory(something, 1)
player.addToInventory(somethingElse, 9)
player.displayInventory()
player.removeFromInventory(somethingElse, 1)
player.removeFromInventory(something, 2)
player.displayInventory()
player.removeFromInventory(somethingElse, -1)
player.removeFromInventory(aThing, 1)
player.displayInventory()
player.accessInventory()
# Equipped item tests
# somethingElse.activateAbility()