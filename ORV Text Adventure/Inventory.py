import Item as item, Text as text

class Inventory:
    def __init__(self):
        self.inventory = {}

    def deleteFromInventory(self, item):
        self.inventory.pop(item)

    def checkDeleteFromInventory(self, item):
        if self.inventory[item] == 0:
            self.deleteFromInventory(item)
    
    def addToInventory(self, item, quantity):
        for i in range(quantity):
            if item in self.inventory:
                self.inventory[item] = self.inventory[item] + 1
            else:
                self.inventory[item] = 1

    def removeFromInventory(self, item, quantity):
        for i in range(quantity):
            if item in self.inventory:
                self.inventory[item] = self.inventory[item] - 1
                self.checkDeleteFromInventory(item)
            else:
                print("ERROR: Attempted to remove item that doesn't exist in inventory")
                return
            
    def accessInventory(self):
        itemName = input("Equip item (q to close): ")
        if itemName == "q":
            print("[Closed inventory]")
            return
        for item in self.inventory:
            if item.getName() == itemName:
                # TODO: equip item
                print(f"Equipped {itemName}")
                return
        print("Item not in inventory")
        self.accessInventory()
        return

    def displayInventory(self):
        text.displayLine()
        print("[Inventory]")

        if len(self.inventory) == 0:
            print("Empty")
            return
        
        for item, quantity in self.inventory.items():
            print(f"{item.getName()} x{quantity}")
        text.displayLine()