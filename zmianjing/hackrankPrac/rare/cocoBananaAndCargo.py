class Solution:
    '''
珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。
珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，
她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。

dd 题
https://leetcode.com/discuss/interview-question/2028170/doordash-phone-screen
    '''
    # binary search nlogn
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low, high = 1 , max(piles)
        while low < high:
            mid = low + (high - low) // 2
            if self.checkHours(piles,mid) > h: ## 用大于， 就说明太小了。 所以左侧逼近
                low = mid + 1 ## approaching left
            else:
                high = mid
        return low

    def checkHours(self, piles, speed):
        hour = 0
        for pile in piles:
            hour += (pile + speed - 1)//speed ## with this , at least one hour we need for a pile

        return hour
    '''
    A conveyor belt has packages that must be shipped from one port to another within days days.
    The ith package on the conveyor belt has a weight of weights[i]. 
    Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
     We may not load more weight than the maximum weight capacity of the ship.
    Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
    '''
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left , right = max(weights) , sum(weights) ## 这里必须是max weight 要不然出现一天装不完一批货的情况的情况
        while left < right:
            mid = left + (right - left) //2
            if self.getDays(weights,mid) > days:
                ## weight is too smaller
                left = mid + 1
            else:
                right = mid

        return left

    def getDays(self, weights, amount):
        days = 1
        cur = 0
        for weight in weights:
            ## 一天肯定能装玩， 所以可以这么做。 超过了 就需要两天
            if cur + weight > amount:
                days += 1
                cur = 0
            cur += weight
        return days


if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed([3,6,7,11],8))