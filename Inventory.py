# Base Class
class Item:
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity += amount
        print(f"{amount} items added .")

    def remove_stock(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"{amount} items removed don't worry.")
        else:
            print("Insufficient stock need to restock asap.")

    def display(self):
        print("\nItem ID :", self.item_id)
        print("Item Name :", self.name)
        print("Quantity :", self.quantity)

        if self.quantity <= 7:
            print("Reminder: Stock is running low. Please restock sai.")

# Inheritance
class FoodItem(Item):
    pass

class ElectronicItem(Item):
    pass

# Object:

food = FoodItem(101, "Rice", 10)

print("FOOD ITEM")
food.display()
food.add_stock(5)
food.remove_stock(8)
food.display()
