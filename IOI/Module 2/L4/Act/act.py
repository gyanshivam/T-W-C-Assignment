# ---- Grocery Cart Manager ----

class GroceryCart:

    # STEP 1 - Parameterized Constructor: runs the moment the cart is created
    def __init__(self, owner, store):
        self.owner = owner
        self.store = store
        self.items = []
        print(f"Cart for '{self.owner}' at '{self.store}' is ready!")

    # STEP 2 - Add an item to the cart
    def add_item(self, item):
        self.items.append(item)
        print(f"'{item}' added to {self.owner}'s cart.")

    # STEP 3 - Remove an item from the cart
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"'{item}' removed from the cart.")
        else:
            print(f"'{item}' was not found in the cart.")

    # STEP 4 - Display all items
    def display(self):
        print(f"\n--- {self.owner}'s Cart at {self.store} ---")
        if self.items:
            for position, item in enumerate(self.items, 1):
                print(f"  {position}. {item}")
        else:
            print("  Cart is empty. Start shopping!")

    # STEP 5 - Destructor: runs automatically when the cart is deleted
    def __del__(self):
        print(f"Cart for '{self.owner}' has been discarded. Happy shopping!")

# Object Creation (constructor fires here)
my_cart = GroceryCart("Aarav", "FreshMart")

# STEP 6 - Menu-driven program using the GroceryCart class
while True:
    print("\n1. Add Item  2. Remove Item  3. View Cart  4. Checkout & Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        my_cart.add_item(item)
    elif choice == "2":
        item = input("Enter item to remove: ")
        my_cart.remove_item(item)
    elif choice == "3":
        my_cart.display()
    elif choice == "4":
        del my_cart   # Destructor fires here
        break
    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")