from typing import List

## https://algo.itcharge.cn/01.Array/03.Array-Binary-Search/02.Array-Binary-Search-02/#_4-2-%E6%8E%92%E9%99%A4%E6%B3%95

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## sanity check
        left , right = 0 , max(piles) ## max , min coco can eat
        while left < right:
            mid = left + (right - left) + 1
            ## speed is not enough to finish all in h
            ## 这里是大于 而不是小于 ， 因为速度越慢 时间越大
            ## 所以我们的目标mid mid 比较小
            if self.canEat(piles,mid) > h :
                left = mid + 1
            else:
                right = mid

        return left

    def canEat(self, piles, speed)->int:
        hours = 0
        for pile in piles:
            ## pile % speed == 0 ? pile / speed : pile / speed + 1;
            ## 核心是向上取整的思想
            hours += (pile + speed - 1) // speed # get ceiling

        return hours




