import unittest
import palindrome as pal

class TestisPalindrome(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertTrue(pal.isPalindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(pal.isPalindrome("No 'x' in Nixon"))
        self.assertTrue(pal.isPalindrome("Was it a car or a cat I saw?"))
        self.assertTrue(pal.isPalindrome("Madam, in Eden, I'm Adam"))
        self.assertTrue(pal.isPalindrome("Never odd or even"))
        self.assertTrue(pal.isPalindrome(""))
        self.assertTrue(pal.isPalindrome("A"))
        self.assertTrue(pal.isPalindrome("Racecar"))
        self.assertTrue(pal.isPalindrome("12321"))

    def test_false_isPalindrome(self):
        self.assertFalse(pal.isPalindrome("Hello, World!"))
        self.assertFalse(pal.isPalindrome("123456"))
        self.assertFalse(pal.isPalindrome("Python"))

if __name__ == '__main__':
    unittest.main()


'''
import palindrome as pal
import logging

logger = logging.getLogger("Palidrome")

test_cases = [
    ("A man, a plan, a canal, Panamaa", True),
    ("No 'x' in Nixon", True),
    ("Was it a car or a cat I saw?", True),
    ("Madam, in Eden, I'm Adam", True),
    ("Never odd or even", True),
    ("Hello, World!", False),
    ("", True),  # An empty string is considered a palindrome
    ("A", True),  # A single character is considered a palindrome
    ("Racecar", True),
    ("12321", True),
    ("123456", False)
]

for s, expected in test_cases:
    result = pal.isPalindrome(s)
    if result == expected:
        #print(f"[PASS]: Yes. {s!r} is a palindrome.!")
        logger.info(f"[PASS]: Yes. {s!r} is a palindrome.!")
    else:
        logger.error(f"[FAIL]: isPalindrome({s!r}) = {result} (Expected: {expected})")
'''