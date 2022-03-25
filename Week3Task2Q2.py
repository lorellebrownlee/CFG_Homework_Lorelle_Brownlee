#Question 2

#I'm setting up my own market stall to sell chocolates. I need a basic till to check the
#prices of different chocolates that I sell.I 've started the program and included the
# chocolates and their prices.Finish the program by asking the user to input an item and then output its price.

#chocolates = {
#   'white': 1.50,
#    'Milk': 1.20,
#    'dark': 1.80,
#    'vegan': 2.00,
#}

chocolates = {
    'white': 1.50,
    'Milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

selected_item = input('What chocolate would you like to make a price enquiry on - white, Milk, dark or vegan?')

# print the cost of the item retrieved from the dictionary to 2 decimal places
if selected_item in chocolates:
    print("This item costs: £{:.2f} ".format(chocolates[selected_item]))

else:
    print("I don't understand.")
