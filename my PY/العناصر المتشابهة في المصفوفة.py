from typing import List
def get_duplicate_elements(arr: List[int]):
    t = []
    for i in arr:
        if arr.count(i) > 1 and i not in t:
            t.append(i)
    return t
print(get_duplicate_elements([1, 3, 5, 5, 9, 9]))