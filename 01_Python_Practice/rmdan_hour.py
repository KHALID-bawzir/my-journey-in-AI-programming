from typing import List
def calculateTotalFastingTime(startTimes: List[str], endTimes: List[str]) -> float:
    total_hour = 0
    for i in range (len(startTimes)):
        start_hour , start_minute = map(int, startTimes[i].split(":"))
        end_hour , end_minute = map(int, endTimes[i].split(":"))
        Shour_to_minute = start_hour * 60 + start_minute
        Ehour_to_minute = end_hour * 60 + end_minute
        total_s = Ehour_to_minute - Shour_to_minute
        total_hour += total_s / 60
    return total_hour

startTimes = ['04:30']
endTimes = ['18:30']
print(calculateTotalFastingTime(startTimes, endTimes))
startTimes = ['05:00']
endTimes = ['18:00']
print(calculateTotalFastingTime(startTimes, endTimes))
startTimes = ['04:45']
endTimes = ['18:15']
print(calculateTotalFastingTime(startTimes, endTimes))
startTimes = ['04:30', '05:00']
endTimes = ['18:30', '18:00']
print(calculateTotalFastingTime(startTimes, endTimes))