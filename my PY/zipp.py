from typing import List
def calculateSacrificeProfit(buyPrices: List[float], sellPrices: List[float]):
    total = 0
    for buy ,sell in zip(buyPrices, sellPrices):
        total += sell - buy
    return total
print(calculateSacrificeProfit([100 ,100], [150 , 150]))