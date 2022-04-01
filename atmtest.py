import unittest
from unittest import TestCase, main, mock
from unittest.mock import patch
from week4task2q1 import enter_pin, withdraw_cash

class TestATM(unittest.TestCase):

#to check correct response to a 5-digit pin being entered
    def test_pin(self):
        my_input = 12345
        result = enter_pin(my_input)
        self.assertEqual(result, "Please try again.")

#to check correct response to user attempting to withdraw more than 100 pounds
    def negative_cash(self):
        my_input = 110
        result = withdraw_cash(my_input)
        self.assertEqual(result, 'NOTE! The account balance cannot be negative!')

#to check correct response to the correct pin being entered
    def correct_pin(self):
        my_input = 1234
        result = enter_pin(my_input)
        self.assertEqual(result, "Correct pin.")


    def correct_cash(self):
        my_input = 90
        expected = 100 - my_input
        result = withdraw_cash(my_input)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

# have also tried to use mock and builtins in the following way:

# import sys
# import unittest
# from unittest import TestCase, main, mock
# from week4task2q1 import enter_pin
#
# class TestATM(unittest.TestCase):
#
#     def test_input_mocking():
#         with unittest.mock.patch('builtins.input', return_value='12234'):
#             assert input() == '12345'
#             print('we got here, so the ad hoc test succeeded')
#
#
#
#     def setUp(self):
#         self.held, sys.stdout = sys.stdout, StringIO()
#
#     @mock.patch('sys.stdout', new_callable=StringIO)
#     def test_pin_too_long(name, mock_stdout):
#         with mock.patch('builtins.input', return_value=name):
#             week4task2q1.enter_pin()
#             assert mock_stdout.getvalue() == 'Please try again.'
#
#     test_pin_too_long('12345')
#
# if __name__ == '__main__':
#     unittest.main()