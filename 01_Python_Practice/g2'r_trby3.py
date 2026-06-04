
from typing import List
def root_check(sqr: float, num: int) -> int:
    if sqr * sqr == num:
        return sqr
    return 0
print(root_check(5, 25))
print(root_check(4, 2))
print(root_check(49, 8))
print(root_check(8, 64))

