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
    '''
        贪心题
        1 对于去第n家restaurant math.min(parking in n -1, waling to n- 1)
        2 if we choose parking in n - 1  we can walk to n or drive to n
        3 if we choose walking to n - 1  we can only drive to n (avoid 2 walking)
        4 drive time is fix , since we need drive car to end
    '''
    drive_time = (restaurant[-1] - restaurant[0])/ DrivingSpeed
    ## two valirable record if we choose walking or driving at n-1 restaunt
    chooseWalking = math.inf # we will choose driving in first one
    chooseDriving = parkingTime[0]
    for i in range(1,len(restaurant)):
        walking_time = (restaurant[i]-restaurant[i-1]) * 2 / WalkingSpeed
        ## n's time depending on n - 1 's status
        ## if we choose wlaking to n, n-1 must be choosing drivieng, can not choose walking in row
        chooseDriving, chooseWalking= min(chooseDriving,chooseWalking) + parkingTime[i], chooseDriving + walking_time
        ## Follow Up是如果可以连着走多家店怎么改，只要改一下更新choosingWalking的逻辑就行。
        # 因为你可以连续走。所以选开车或者走路最省时间的就可以了， 对于每家店的walkingtime 固定的。
        #chooseDriving, chooseWalking = min(chooseDriving, chooseWalking) + parkingTime[i], min(chooseDriving, chooseWalking) + walking_time

    return min(chooseWalking,chooseDriving) + drive_time


restaurant = [0, 3, 5, 10, 15]
parkingTime = [3, 3, 4, 5, 1]
WalkingSpeed = 1
DrivingSpeed = 2
print(pickingUpTime(restaurant,parkingTime,WalkingSpeed,DrivingSpeed))