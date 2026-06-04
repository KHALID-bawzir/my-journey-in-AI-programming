from typing import List
def longestAlternatingSubstring(digits: str):
    for i in digits:
        if digits[i] % 2 == 0 and digits[i+1] % 2 != 0:
            print(i)
    return i
print(longestAlternatingSubstring("12345"))
