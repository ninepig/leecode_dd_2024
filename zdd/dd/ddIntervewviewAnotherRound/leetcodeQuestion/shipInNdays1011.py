class Solution:
    '''
    ability to ship in N days
    '''
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if not weights or len(weights) == 0: return -1
        right = sum(weights)
        left = max(weights)  ## 不能取0,必须是max weight

        while left < right:
            mid = left + (right - left) // 2
            if self.countDays(mid,weights) <= days:
                right = mid # less than days, so we can reduce the max dayily shipment
            else:
                left = mid + 1 # we can not made that, so need increasing
        return left

    ## 这个方法比较好
    def countDays(self, mid,weights):
        days = 1
        cur = 0
        for weight in weights:
            if cur + weight > mid:
                days += 1
                cur = 0
            cur += weight
        return days

