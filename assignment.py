# Inventory Management System (IMS)

### 1. Inventory Manageement; Inventory as Class

class Inventory:
    # This is a constructor for a class which initializes the items data.
    def __init__(self):
        self.items = {}  # Dictionary to hold item information.
 
    def add_item(self, item_name, quantity, price):
        """Add a new item to the inventory."""
        if item_name in self.items:
            print(f"Item '{item_name}' already exists. Updating quantity.")
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'quantity': quantity, 'price': price}
        print(f"Item '{item_name}' added/updated with {quantity} quantity at ${price} each.")

    def update_item(self, item_name, quantity):
        """You need to modify the amount of a current item."""
        self.items[item_name]['quantity'] += quantity if item_name in self.items else 'wrong item'
        print(f"Item '{item_name}' updated by adding {quantity} more items.") if item_name in self.items else print(f"Item '{item_name}' is not available to update.")
    
    def remove_item(self, item_name):
        """Remove item from inventory."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Item '{item_name}' has been deleted from inventory.")
        else:
            print(f"Item '{item_name}' does not exist in inventory.")

    def view_inventory(self):
        """Show all the available items in the stock."""
        if len(self.items) == 0:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            for item_name, details in self.items.items():
                print(f"{item_name}: {details['quantity']} units at ${details['price']} each")

    def get_item_price(self, item_name):
        """Get the price of an item."""
        if item_name in self.items:
            return self.items[item_name]['price']
       
