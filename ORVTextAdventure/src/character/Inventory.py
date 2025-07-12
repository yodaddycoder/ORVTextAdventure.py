from helper import Text as text

class Inventory:
    def __init__(self):
        self.inventory = {}
        self.equipped = None

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

    def displayInventory(self):
        text.displayLine()
        print("[Inventory]")

        if len(self.inventory) == 0:
            print("Empty")
            return
        
        for item, quantity in self.inventory.items():
            print(f"{item.name} x{quantity}")
        text.displayLine()

    def unequipItem(self):
        self.addToInventory(self.equipped, 1)
    
    def equipItem(self, item):
        self.removeFromInventory(item, 1)
        if (self.equipped != None):
            self.unequipItem()
        self.equipped = item
        print(f"Equipped {item.name}")
    
    def deleteEquipped(self):
        self.equipped = None

    def showEquipped(self):
        if (self.equipped == None):
            print("You are not using anything")
            return
        print(f"You have a(n) {self.equipped.name}")

    def accessInventory(self):
        self.displayInventory()
        itemName = input("Select item (q to close): ")
        if itemName == "q":
            print("[Closed inventory]")
            return
        for item in self.inventory:
            if item.name == itemName:
                self.inventoryAction(item)
                self.accessInventory()
                return
        print("Item not in inventory")
        self.accessInventory()
        return
    
    def inventoryAction(self, item):
        action = input("1 to equip, 2 to view details (q to quit): ")
        if action == "q":
            return
        if action == "1":
            self.equipItem(item)
            return
        if action == "2":
            item.displayDetails()
            return
        print("That's not a valid action")