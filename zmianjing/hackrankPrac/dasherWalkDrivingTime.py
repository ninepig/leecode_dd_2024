import math


class Solution:
    def getTimeTodeliver(self, parking, restaurant, walkingSpeed, drivingSpeed):
        ## sanity check
        if not parking or not restaurant or walkingSpeed == 0 or drivingSpeed == 0:
            raise Exception("Wroing input")

        '''
        greedy 
        driving time is fixed  no mater we walk or drive
        so we need to figure out how to get less time by using walk or park
        to n's restuanlt , we can drive or walk if we drive to n-1 .
         if walk to n-1, we can only choose drive to n
        '''
        drivingTime = (restaurant[-1] - restaurant[0]) / drivingSpeed
        chooseWalking = math.inf
        chooseDriving = parking[0]

        for i in range(1, len(restaurant)):
            ## 不需要向下取整
            walkingTime = (restaurant[i] - restaurant[i - 1]) / walkingSpeed * 2  ## if we walkt to n , walking time is
            chooseDriving, chooseWalking = min(chooseWalking, chooseDriving) + parking[i], chooseDriving + walkingTime
            # if we can walk mult restauant
            # chooseDriving, chooseWalking = min(chooseWalking, chooseDriving) + parking[i], min(chooseDriving,chooseWalking) + walkingTime

        return min(chooseDriving, chooseWalking) + drivingTime


restaurant = [0, 3, 5, 10, 15]
parkingTime = [3, 3, 4, 5, 1]
WalkingSpeed = 1
DrivingSpeed = 2
sol = Solution()
print(sol.getTimeTodeliver(parkingTime, restaurant, WalkingSpeed, DrivingSpeed))