'''
很好的应用题
遍历数组 bloomDay。
如果 bloomDay[i] 小于等于天数 days。就将花朵数量 + 1。
当能摘的花朵数等于 k 时，能摘的花束数目 + 1，花朵数量置为 0。
如果 bloomDay[i] 大于天数 days。就将花朵数置为 0。
最后判断能摘的花束数目是否大于等于 m。
整个算法的步骤如下：

如果 m * k 大于 len(bloomDay)，说明无法满足要求，直接返回 -1。
使用两个指针 left、right。令 left 指向 min(bloomDay)，right 指向 max(bloomDay)。代表待查找区间为 [left, right]。
取两个节点中心位置 mid，判断是否能在 mid 天制作 m 束花。
如果不能，则将区间 [left, mid] 排除掉，继续在区间 [mid + 1, right] 中查找。
如果能，说明天数还可以继续减少，则继续在区间 [left, mid] 中查找。
当 left == right 时跳出循环，返回 left。
'''

class Solution:
    def canMake(self, bloomDay, days, m, k):
        count = 0
        flower = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= days:
                flower += 1
                if flower == k:
                    count += 1
                    flower = 0
            else:
                flower = 0
        return count >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m > len(bloomDay) / k:
            return -1

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2
            if not self.canMake(bloomDay, mid, m, k):
                left = mid + 1
            else:
                right = mid

        return left