#Name:logan
#Class: 6th Hour
#Assignment: Scenario 7

#Import all of Scenario 6 here
from Scenario6 import stats
import Scenario6
listAverage = 0

def final_average():
    global listAverage
    listAverage = (stats[5]+stats[4]+stats[3]+stats[2]+stats[1]+stats[0])
    listAverage = listAverage//6
    return listAverage

final_average()

print(listAverage)