
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
       self.total_items = {'hairbrush': 1.50,'toothpaste': 0.90, 'hair gel': 1.25, 'dental floss': 1.00, 'sun block': 4.30, 'shampoo': 2.10, 'conditioner': 2.05, 'toothbrush':3.00}
       self.total_price = 0
       self.discount = {'20OFF': 0.20, '10OFF' : 0.10, '5OFF' : 0.05}
       self.receipt_items = []

   # add an item to a list
   def add_item(self):
       item = input('What would you like to buy?')
       if item in self.total_items:
           self.receipt_items.append(item)
       more_items = input('Would you like to add an item, remove an item, or continue with the transaction? A to add, R to remove or C to continue or X to clear all items.')
       if more_items == 'A':
           self.add_item()
       elif more_items == 'R':
           self.remove_item()
       elif more_items == 'C':
           self.show_items()
       elif more_items == 'X':
           self.reset_register()

   #remove an item from the list
   def remove_item(self):
       removed_item = input('What item would you like to remove?')
       if removed_item in self.receipt_items:
           self.receipt_items.remove(removed_item)
       next_step = input('Would you like to add an item, remove an item, or continue with the transaction? A to add, R to remove, C to continue or X to clear all items.')
       if next_step == 'A':
           self.add_item()
       elif next_step == 'R':
           self.remove_item()
       elif next_step == 'C':
           self.show_items()
       elif next_step == 'X':
           self.reset_register()

   # multiply total by discount as % and subtract this from total
   def apply_discount(self):
       discount_code = input('Please enter a coupon code: ')
       if discount_code in self.discount:
           self.total_price = self.total_price * (1 - self.discount[discount_code])
       else:
           print('This coupon code is invalid.')
       print('The total is: £', self.total_price)

   # sum all item prices and print the total
   def get_total(self):
       for receipt_item in self.receipt_items:
           if receipt_item in self.total_items:
               self.total_price = self.total_price + self.total_items[receipt_item]
       print('The total is £', self.total_price)
       self.apply_discount()

   # list/print all items on receipt
   def show_items(self):
       print('Item summary: ')
       for receipt_item in self.receipt_items:
           print(receipt_item, '£', self.total_items[receipt_item])
       self.get_total()

   # remove all items and return balance to 0
   def reset_register(self):
       self.receipt_items.clear()
       print('All items cleared.')



# ADD
p1 = CashRegister()
p1.add_item()


# EXAMPLE code run:

# What would you like to buy?hairbrush
# Would you like to add an item, remove an item, or continue with the transaction? A to add, R to remove or C to continue or X to clear all items.A
# What would you like to buy?toothpaste
# Would you like to add an item, remove an item, or continue with the transaction? A to add, R to remove or C to continue or X to clear all items.A
# What would you like to buy?sun block
# Would you like to add an item, remove an item, or continue with the transaction? A to add, R to remove or C to continue or X to clear all items.C
# Item summary:
# hairbrush £ 1.5
# toothpaste £ 0.9
# sun block £ 4.3
# The total is £ 6.699999999999999
# Please enter a coupon code: 20OFF
# The total is: £ 5.359999999999999