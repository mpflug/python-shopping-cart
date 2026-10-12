
# Name: Michelle Pflug
# Date: October 10, 2026
# Purpose: Create an online shopping cart program


# Step 1: Create the ItemToPurchase class
class ItemToPurchase:

    # Default constructor
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    # Print item cost
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:g} = ${total:g}")


# Step 2: Create the ShoppingCart class
class ShoppingCart:

    # Parameterized constructor
    def __init__(self, cust_name="none", day_date="January 1, 2025"):
        self.customer_name = cust_name
        self.current_date = day_date
        self.cart_items = []

    # Add item to cart
    def add_item(self, item):
        self.cart_items.append(item)

    # Remove item from cart
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return

        print("Item not found in cart. Nothing removed.")

    # Modify item quantity
    def modify_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                cart_item.item_quantity = item.item_quantity
                return

        print("Item not found in cart. Nothing modified.")

    # Return total number of items
    def get_num_items_in_cart(self):
        total_quantity = 0

        for item in self.cart_items:
            total_quantity += item.item_quantity

        return total_quantity

    # Return total cost of cart
    def get_cost_of_cart(self):
        total_cost = 0

        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity

        return total_cost

    # Display shopping cart
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

            print(f"Number of Items: {self.get_num_items_in_cart()}")
            print()
            print(f"Total: ${self.get_cost_of_cart():g}")


# Step 4: Display menu
def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("o - Output shopping cart")
    print("q - Quit")


# Step 5: Execute menu selection
def execute_menu(menuOp, theCart):

    # Add item to cart
    if menuOp == "a":
        print("ADD ITEM TO CART")

        item = ItemToPurchase()

        item.item_name = input("Enter the item name: ")
        item.item_price = float(input("Enter the item price: "))
        item.item_quantity = int(input("Enter the item quantity: "))

        theCart.add_item(item)

    # Remove item from cart
    elif menuOp == "r":
        print("REMOVE ITEM FROM CART")

        item_name = input("Enter name of item to remove: ")
        theCart.remove_item(item_name)

    # Change item quantity
    elif menuOp == "c":
        print("CHANGE ITEM QUANTITY")

        item = ItemToPurchase()

        item.item_name = input("Enter the item name:")
        item.item_quantity = int(input("Enter the new quantity: "))

        theCart.modify_item(item)

    # Output shopping cart
    elif menuOp == "o":
        print("OUTPUT SHOPPING CART")
        theCart.print_total()


# Step 3 and Step 5a: Main program
if __name__ == "__main__":

    # Get customer information
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")

    # Create shopping cart
    my_cart = ShoppingCart(customer_name, current_date)

    # Display customer information
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print()
    
    # Initialize menu choice
    menu_choice = ""

    # Continue until user selects Quit
    while menu_choice != "q":

        print_menu()
        print()
