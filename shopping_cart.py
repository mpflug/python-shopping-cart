# Name: Michelle Pflug
# Date: October 10, 2026
# Purpose: Create an online shopping cart program


class ItemToPurchase:

    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:g} = ${total:g}")


class ShoppingCart:

    def __init__(self, cust_name="none", day_date="January 1, 2025"):
        self.customer_name = cust_name
        self.current_date = day_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return

        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                cart_item.item_quantity = item.item_quantity
                return

        print("Item not found in cart. Nothing modified.")

    def print_total(self):
        total_quantity = 0
        total_cost = 0

        for item in self.cart_items:
            total_quantity += item.item_quantity
            total_cost += item.item_price * item.item_quantity

        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {total_quantity}")
        print()

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print()
        print(f"Total: ${total_cost:g}")


def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("o - Output shopping cart")
    print("q - Quit")


def execute_menu(menuOp, theCart):

    if menuOp == "a":
        print("ADD ITEM TO CART")

        item = ItemToPurchase()

        item.item_name = input("Enter the item name:\n")
        item.item_price = float(input("Enter the item price:\n"))
        item.item_quantity = int(input("Enter the item quantity:\n"))

        theCart.add_item(item)

    elif menuOp == "r":
        print("REMOVE ITEM FROM CART")

        item_name = input("Enter name of item to remove:\n")

        theCart.remove_item(item_name)

    elif menuOp == "c":
        print("CHANGE ITEM QUANTITY")

        item = ItemToPurchase()

        item.item_name = input("Enter the item name:\n")
        item.item_quantity = int(input("Enter the new quantity:\n"))

        theCart.modify_item(item)

    elif menuOp == "o":
        print("OUTPUT SHOPPING CART")
        theCart.print_total()


if __name__ == "__main__":

    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    my_cart = ShoppingCart(customer_name, current_date)

    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print()

    menu_choice = ""

    while menu_choice != "q":

        print_menu()
        print()

        menu_choice = input("Choose an option:\n")

        while menu_choice not in ["a", "r", "c", "o", "q"]:
            menu_choice = input("Choose an option:\n")

        if menu_choice != "q":
            print()
            execute_menu(menu_choice, my_cart)
            print()