from character import Character as c, Item as item

# Character creation test
player = c.MainCharacter("Boo")
player.displayAttributesWindow()
# Inventory tests
def basicAbility(): print(f"Used a basic ability!")
something = item.Item("something", False, item.Grade.A, basicAbility)
somethingElse = item.Item("somethingElse", True, item.Grade.A, basicAbility)
aThing = item.Item("aThing", True, item.Grade.A, basicAbility)

player.inventory.displayInventory()
player.inventory.addToInventory(something, 1)
player.inventory.addToInventory(somethingElse, 9)
player.inventory.displayInventory()
player.inventory.removeFromInventory(somethingElse, 1)
player.inventory.removeFromInventory(something, 2)
player.inventory.displayInventory()
player.inventory.removeFromInventory(somethingElse, -1)
player.inventory.removeFromInventory(aThing, 1)
player.inventory.addToInventory(something, 1)
player.inventory.displayInventory()
# Equipped item tests
player.useEquipped()
player.inventory.accessInventory() # Equip somethingElse
player.inventory.showEquipped()
player.useEquipped()
player.inventory.displayInventory()
player.inventory.accessInventory() # Equip something
player.inventory.showEquipped()
player.useEquipped()
player.inventory.displayInventory()