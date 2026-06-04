from typing import List
def countdown(num: int):
    sortw = list(range(num , -1 , -3))
    sortf = [x for x in sortw if x % 2 == 0 and x != num]
    if not sortf :
        return [0]
    return sorted(sortf)
print(countdown(103))