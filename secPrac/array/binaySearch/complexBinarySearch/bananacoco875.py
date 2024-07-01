class Solution:
    #二分法应用题
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) //2
            if not self.canEat(mid,piles,h):
                left = mid + 1
            else:
                right = mid

        return left

    def canEat(self, mid, piles, h):
        time = 0
        for pile in piles:
            time += (pile + mid - 1) // mid # 至少需要 1. 就算pile只有1 也需要1小时

        return time <= h
