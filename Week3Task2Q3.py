# Write a program that simulates a lottery. The program should have a list of seven
# numbers   that   represent   a   lottery   ticket.   It   should   then   generate   seven   random
# numbers. After comparing the two sets of numbers, the program should output a
# prize based on the number of matches:

# £20 for three matching numbers
# £40 for four matching numbers
# £100 for five matching numbers
# £10000 for six matching numbers
# £1000000 for seven matching numbers


import random

#
number_draw = []
user_ticket = []

count_correct = 0

#draws 7 random numbers and adds them to the empty list 'number_draw'
for number in range(0, 7):
    random_num = random.randint(1, 50)
    number_draw.append(random_num)

#asks the user for 7 numbers and adds them to the empty list 'user_ticket'
for num in range(0, 7):
    user_number = int(input('Please enter a number between 1 and 50:'))
    user_ticket.append(user_number)

#for each combination of values between the randomly drawn numbers and the user chosen numbers, checks if they match
# for every match, the count of matching numbers increases by 1
for lotto_num in number_draw:
    for user_number in user_ticket:
        if user_number == lotto_num:
            count_correct = count_correct + 1

#dictionary of matching number counts and prize money
prize_money = {
    0: '£0',
    1: '£0',
    2: '£0',
    3: '£20',
    4: '£40',
    5: '£100',
    6: '£10000',
    7: '£1000000'
}
# matches the count of matching numbers to its prize number value and prints the result
for key, value in prize_money.items():
    if key == count_correct:
        print('You have matched {} numbers and you have won {}.'.format(key, value))