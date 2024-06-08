#Palindrome

def isPalindrome(s: str) -> bool:
    clean_s = "".join(c.lower() for c in s if c.isalnum())
    return clean_s == clean_s[::-1]

input_str = "123454321"
print(isPalindrome(input_str))
