class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def addItem(self, itemName, quantity):
        self.inventory[itemName] = quantity

    def checkStockLevel(self, itemName):
        return self.inventory.get(itemName, 0)

    def alertLowStock(self, itemName):
        if self.checkStockLevel(itemName) < 5:
            return f"Warning: {itemName} is running low."
        return f"{itemName} has enough stock."