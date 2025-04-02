from cart import Cart
from data import inventory

class CartFunctionality:

    def __init__(self, cart: Cart):
        self.cart = cart
        self.inventory = inventory

    def check_inventory(self, item_name, qty):
        if item_name in self.inventory:
            if self.inventory[item_name]["qty"] >= qty:
                self.inventory[item_name]["qty"] -= qty
                return True
            else:
                print(f"Not enough stock for '{item_name}'")
                return False
        print(f"{item_name} is not found in inventory.")
        return False

    def add_item(self, item_name, qty):
        if self.check_inventory(item_name, qty):
            if item_name in self.cart.cart_items:
                #if an existing item, just add the qty
                self.cart.cart_items[item_name] += qty
            else:
                # if a new item, just add the item with qty
                self.cart.cart_items[item_name] = qty
            print(f"Added {qty} x {item_name}")

    def remove_item(self, item_name, qty):
        item_list = []
        for key in self.cart.cart_items:
            item_list.append(key)

        if item_name in item_list:
            if self.cart.cart_items[item_name] <= qty:
                self.cart.cart_items.pop(item_name)
            else:
                self.cart.cart_items[item_name] -= qty
        print(f"{item_name} x {qty} successfully removed!")

    def calc_total_sum(self):
        total = 0
        for item in self.cart.cart_items:
            qty = self.cart.cart_items[item]
            price = self.inventory[item]["price"]
            total += qty * price
        return total

