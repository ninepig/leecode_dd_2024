'''
经典二分法应用题


A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i].
Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
 e may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
'''

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        min = max(weight)
        max = sum(weight)
        '''
        left = max(weights)
        right = sum(weights)
        while left < right :
            mid = left + (right - left) // 2
            if self.getDays(weights,mid) > days:
                left = mid + 1
            else:
                right = mid

        return left

    def getDays(self, weights, cap):
        need = 1
        cur_weight = 0
        for w in weights:
            if (cur_weight + w) > cap:
                need += 1
                cur_weight = 0
            cur_weight += w

        return need


    '''吃香蕉 ---》 这个题有个特点 
    
     If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour
    如果 pile 小于speed 也需要话1个小时 没法多
     
    也就是每个小时最多就是吃pile里的香蕉
    
    time += (pile + speed - 1) // speed --> make sure we have at least 1 hour for eating this pile
    '''
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = min(piles)
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            ## eating rate too low
            if self.getEatHour(piles,mid) > h:
                left = mid + 1
            else:
                right = mid

        return left

    def getEatHour(self, piles, speed):
        hour = 0
        for pile in piles:
            hour += (pile + speed - 1)//speed

        return hour






