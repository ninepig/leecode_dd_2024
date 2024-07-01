'''
二分法应用题

船最小的运载能力，最少也要等于或大于最重的那件包裹，即 max(weights)。最多的话，可以一次性将所有包裹运完，即 sum(weights)。船的运载能力介于 [max(weights), sum(weights)] 之间。

我们现在要做的就是从这个区间内，找到满足可以在 D 天内运送完所有包裹的最小载重量。

可以通过二分查找的方式，找到满足要求的最小载重量。
'''

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) >> 1
            days = 1
            cur = 0
            for weight in weights:
                if cur + weight > mid:
                    days += 1
                    cur = 0
                cur += weight

            if days <= D:
                right = mid
            else:
                left = mid + 1
        return left