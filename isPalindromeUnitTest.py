import unittest
import palindrome


class MyPalindromeTests(unittest.TestCase):

    # tests if the function handles a palindrome with spaces or characters
    def test_string_characters(self):
        result = palindrome.isPalindrome('! hannah !')
        self.assertEqual(True, result)

    # tests if function delivers a True result if isPalindrome parameter is a palindrome
    def test_true_result(self):
        result = palindrome.isPalindrome('hannah')
        self.assertEqual(True, result)  # add assertion here

    # tests if function delivers a Fail result if isPalindrome parameter is not a palindrome
    def test_false_result(self):
        result = palindrome.isPalindrome('banana')
        self.assertEqual(False, result)


if __name__ == '__main__':
    unittest.main()
