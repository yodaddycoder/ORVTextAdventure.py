from character import Character as c, Item as item

### Character creation test
player = c.MainCharacter("Boo")
player.displayAttributesWindow()
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
# something = item.Item("something", False, item.Grade.A, basicAbility)
# something.addDescription("This item was created for some reason idk.")
# something.addAbilityDescription("Wow this item does something.")

# somethingElse = item.Item("somethingElse", True, item.Grade.D, basicAbility)
# somethingElse.addDescription("This item was created for some reason idk.")
# somethingElse.addAbilityDescription("Wow this item does something. Oh btw it can only be used once.")

# aThing = item.Item("aThing", True, item.Grade.Constellation, basicAbility)

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