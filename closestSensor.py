def findClosestSensor(readings):
    maxReading = 0
    maxIndex = 0
    for index in range(len(readings)):
        if readings[index] > maxReading:
            maxReading = readings[index]
            maxIndex = index
    sensorIndex = maxIndex
    if maxReading >= 20:
        return sensorIndex
    else:
        return -1

print(findClosestSensor([211, 285, 92, 119, 3, 0, 0]))
