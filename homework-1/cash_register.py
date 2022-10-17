"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):
        self.total_items = []

    def add_item(self, new_item, new_price):
        self.total_items.append({"Name": new_item, "Price": new_price})
        print("Item added successfully")

    def remove_item(self, item_to_remove):
        for item in self.total_items:
            if item['Name'] == item_to_remove:
                self.total_items.remove(item)
                print(f"Item has been removed from cart")

    def get_total(self):
        total_price = 0
        for item in self.total_items:
            total_price += item["Price"]
        print(f"Your total amount is to pay {total_price}")
        return total_price

    def apply_discount(self, discount):
        total_price = self.get_total()
        if discount != 0:
            total_price -= total_price * (discount/100)
            print(f"Total price after discount is {total_price}")
        else:
            print(f"Total price without discount is {total_price}")

    def show_items(self):
        print(f"Total items are {self.total_items} ")

    def reset_register(self):
        self.total_items.clear()
        print("cash register is reset now!!")


# starting cash register
my_purchase = CashRegister()
my_purchase.show_items()
my_purchase.get_total()

# Item added
my_purchase.add_item('hat', 2.0)
my_purchase.add_item('T-shirt', 4.5)
my_purchase.show_items()
my_purchase.get_total()

# Item removed
my_purchase.remove_item('T-shirt')
my_purchase.show_items()
my_purchase.get_total()

# Discount applied
my_purchase.apply_discount(40)
my_purchase.show_items()

# Cash register reset
my_purchase.reset_register()
my_purchase.show_items()
