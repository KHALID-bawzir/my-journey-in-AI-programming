from typing import List
def sub_arrays(arr1: List[int], arr2: List[int]):
     result = [b - a for a, b in zip(arr1, arr2)]
     return result

s = sub_arrays([3 , 4], [3 , 6])
print(s)