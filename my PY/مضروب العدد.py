from typing import List
def factorial(number: int):
    total = 1
    for i in range(1, number + 1):
        total *= i
    return total
print(factorial(5))
