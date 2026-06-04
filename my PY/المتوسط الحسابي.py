from typing import List
def average(values: List[int]):
    return sum(values) / len(values)
values = [2, 4, 9, 23, 435]
print(average(values))