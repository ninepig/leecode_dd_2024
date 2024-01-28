import math


'''
https://www.1point3acres.com/bbs/thread-940762-1-1.html
之前面的同一题，其实思路还挺简单的，如果N-1选择了停车，那么第N家店可以走路提或者开车提，如果N-1选择了走路，那么N必须停车。只需要记录前一家店两种选择的两个累积最小时间就行。
Follow Up是如果可以连着走多家店怎么改，只要改一下更新choosingWalking的逻辑就行。
后面给主动提了个followup，如果可以选择开回道路入口处离开，怎么改，思路大概就是DrivingTime不再fix，和最后的停车点相关。
'''
restaurant = [0, 3, 5, 10, 15]
parkingTime = [3, 3, 4, 5, 1]
WalkingSpeed = 1
DrivingSpeed = 2

def pickingUpTime(restaurant, parkingTime, WalkingSpeed, DrivingSpeed):
    N = len(restaurant)
    drivingTime = (restaurant[-1] - restaurant[0]) / DrivingSpeed
    chooseParking = parkingTime[0]
    chooseWalking = math.inf

    for i in range(1, N):
        walkingTime = 2 * (restaurant[i] - restaurant[i-1])/ WalkingSpeed
        chooseParking, chooseWalking =  min(chooseParking, chooseWalking) + parkingTime[i], chooseParking + walkingTime

    return min(chooseParking, chooseParking) + drivingTime

time = pickingUpTime(restaurant, parkingTime, WalkingSpeed, DrivingSpeed)
print(time)