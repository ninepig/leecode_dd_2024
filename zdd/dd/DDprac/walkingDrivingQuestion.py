import math


'''

有一个直线的街道，街道上有n个餐厅，有一个array来表示餐厅的坐标，如：restaurant: [0, 3, 5, 10, 15]
你是一个开车的外卖小哥，你要去每个餐厅取餐，起始点是第一个餐厅，终点是最后一个餐厅 （经过询问之后，面试官小哥告诉我取餐是从餐厅0->n-1按顺序取）
你会开车，你也会走路，input给开车速度&走路速度
每个餐厅有parking time，用一个array表示，如：parkingTime: [3, 3, 4, 5, 1]
在每个餐厅取餐的时候，你可以选择：
Option 1: 开车停到该餐厅（花费对应的driving time），Park（花费对应的Parking Time），取餐（不花时间）
Option 2: 车子停在上一个餐厅，走路去该餐厅（花费walking time），取餐，再走回去上一个餐厅（再次花费walking time）



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

    return min(chooseParking, chooseWalking) + drivingTime

time = pickingUpTime(restaurant, parkingTime, WalkingSpeed, DrivingSpeed)
print(time)