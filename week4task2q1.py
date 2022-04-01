
# #TASK 2 (Exception Handling)
#
# #Question 1
# Simple ATM program
# Using exception handling code blocks such as try/ except / else / finally, write a program that simulates an ATM machine to withdraw money.
# (NB: the more code blocks the better, but try to use at least two key words e.g. try/except)
# Tasks:
# 1.       Prompt user for a pin code
# 2.       If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again. You can give a user a maximum of 3 attempts and then exit a program.
# 3.       Set account balance to 100.
# 4.       Now we need to simulate cash withdrawal
# 5.       Accept the withdrawal amount
# 6.       Subtract the amount from the account balance and display the remaining balance (NOTE! The balance cannot be negative!)
# 7.       However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to raise an error an exit the program.



account_balance = 100


def withdraw_cash():
   withdrawal_amount = int(input("Please enter withdrawal amount:"))
   end_balance = account_balance - withdrawal_amount
   try:
       if withdrawal_amount > account_balance:
           raise Exception

   except:
       print('NOTE! The account balance cannot be negative!')
       withdraw_cash()

   else:
       print('Withdrawal accepted. Your remaining balance is {}.'.format(end_balance))
       quit()


def enter_pin():

   pin_attempts = 0
   for number in range(0, 3):
       user_pin = int(input('Please enter your 4-digit pin:'))
       try:
           if user_pin != 1234:
               pin_attempts += 1
               return "Please try again."
               raise Exception

       except:


           def incorrect_pin():
               try:
                   if pin_attempts >= 3:
                       raise Exception
               except:
                   print("Pin entered incorrectly too many times.")
                   quit()
           incorrect_pin()

       else:
           print("Correct pin.")
           withdraw_cash()



#enter_pin()


