import math

'''
https://www.1point3acres.com/bbs/thread-940762-1-1.html
其实思路还挺简单的，如果N-1选择了停车，那么第N家店可以走路提或者开车提，如果N-1选择了走路，那么N必须停车。
只需要记录前一家店两种选择的两个累积最小时间就行。Follow Up是如果可以连着走多家店怎么改，只要改一下更新choosingWalking的逻辑就行。
后面给主动提了个followup，如果可以选择开回道路入口处离开，怎么改，思路大概就是DrivingTime不再fix，和最后的停车点相关


最基本的题
1 只能走一家店 就必须回去。 逻辑就通了 （先和面试官确认）， 这个是个贪心。因为只考虑一家店
2 能走多家店？ 需要想一想 感觉就是个DP了
'''
def pickingUpTime(restaurant, parkingTime, WalkingSpeed, DrivingSpeed):
    N = len(restaurant)
    ## driving time 是固定的 ，因为你最终一定要把车开过去
    drivingTime = (restaurant[-1] - restaurant[0]) / DrivingSpeed
    ## 第一家店是肯定开车过去的
    chooseParking = parkingTime[0]
    ## 第一家店的走路时间肯定是无限， 因为不会走过去
    chooseWalking = math.inf

    ##记录的是前一家店到达所用时间
    for i in range(1, N):
        walkingTime = 2 * (restaurant[i] - restaurant[i-1])/ WalkingSpeed
        # 这里同时更新 就不会有问题了
        # 记录前一个状态的最低值
        # 如果你n-1店选择了走路， 那你n店只能是 开车（选择停车） 如果你n-1是开车的 ，那你就是开车或者走路。 避免走2段路的时间
        chooseParking, chooseWalking = min(chooseParking, chooseWalking) + parkingTime[i], chooseParking + walkingTime

    return min(chooseParking, chooseWalking) + drivingTime


restaurant = [0, 3, 5, 10, 15]
parkingTime = [3, 3, 4, 5, 1]
WalkingSpeed = 1
DrivingSpeed = 2
time = pickingUpTime(restaurant, parkingTime, WalkingSpeed, DrivingSpeed)
print(time)