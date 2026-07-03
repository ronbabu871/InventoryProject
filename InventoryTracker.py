class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def addItem(self, itemName, quantity):
        self.inventory[itemName] = quantity