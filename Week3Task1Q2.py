#I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5

#deposit. I've written a program to check that I can afford the cost, but something

#doesn't seem right. Have a look at my program and work out what I've done wrong


#Answer:
#my_money should have the input converted from string to integer
my_money = int(input('How much money do you have? '))

#boat cost needs an underscore: boat_cost
boat_cost =20+5

#my_money should be >= to boat_cost and if should start with a lower case i
if my_money >= boat_cost:

    print('You can afford the boat hire')

else:

#there should be a closing parenthesis at the end of the print function call
    print('You cannot afford the board hire')
