import Character as c
import Item as item

# Character creation test
player = c.MainCharacter("Boo")
player.displayAttributesWindow()
# Inventory tests
something = item.Item("something")
somethingElse = item.Item("somethingElse")

player.displayInventory()
player.addToInventory(something, 1)
player.addToInventory(somethingElse, 9)
player.displayInventory()
player.removeFromInventory(somethingElse, 1)
player.removeFromInventory(something, 2)
player.displayInventory()
player.removeFromInventory(somethingElse, -1)
player.removeFromInventory(item.Item("aThing"), 1)
player.displayInventory()