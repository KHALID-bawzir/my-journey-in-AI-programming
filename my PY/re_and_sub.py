import re
from typing import List
def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub(r'[^a-z0-9]','',s)
    return s == s[::-1]
print(isPalindrome('A man, a plan, a canal: Panama'))  # True
print(isPalindrome('race a car'))  # False
print(isPalindrome(' '))  # True
print(isPalindrome('madam'))  # True

