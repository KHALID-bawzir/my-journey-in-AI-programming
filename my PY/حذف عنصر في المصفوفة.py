from typing import List
def delete_element_in_array(arr: List[int], index: int):
    del arr[index]
    return arr
print(delete_element_in_array([1,2,3,4,5],0,))