from data import inventory
from product import Product
from cart import Cart
from cart_functionality import CartFunctionality

my_cart = Cart()
cart_functionality = CartFunctionality(my_cart)

inventory_items = []
for item in inventory:
    inventory_items.append(item)


cart_functionality.add_item(
    inventory_items[0],
    2
)

cart_functionality.add_item(
    inventory_items[3],
    10
)

cart_functionality.remove_item(
    inventory_items[0],
    1
)

print("ITEMS IN CART: ", my_cart.cart_items)

print(cart_functionality.calc_total_sum())

#TODO: Revise all the code in response to the data structure change
#TODO: Proceed with final functionality of calc_total_sum
#Check_inventory is completed

