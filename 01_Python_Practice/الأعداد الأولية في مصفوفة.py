from typing import List
def primes_nums(numbers: List[int]):
    total = []
    for num in numbers:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            total.append(num)
    return total

print(primes_nums([1, 2, 3, 4, 5, 6]))