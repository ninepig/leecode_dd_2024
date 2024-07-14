## https://algo.itcharge.cn/01.Array/03.Array-Binary-Search/02.Array-Binary-Search-02/#_4-2-%E6%8E%92%E9%99%A4%E6%B3%95
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        ## santity check
        left = 0
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if self.canShip(weights,mid) > days: ## mid is too smaller, we can not finish in days
                left = mid + 1
            else:
                right = mid
        return left

    def canShip(self, weights, cap):
        days = 0
        cur = 0
        for weight in weights:
            if weight + cur > cap : ## if we reach cap
                days += 1
                cur = 0
            cur += weight ## if we dont reach, added
        return days

