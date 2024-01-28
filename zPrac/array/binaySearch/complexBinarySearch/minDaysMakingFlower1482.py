
'''
遍历数组 bloomDay。
如果 bloomDay[i] 小于等于天数 days。就将花朵数量 + 1。
当能摘的花朵数等于 k 时，能摘的花束数目 + 1，花朵数量置为 0。
如果 bloomDay[i] 大于天数 days。就将花朵数置为 0。
最后判断能摘的花束数目是否大于等于 m。

好题, 逻辑思维要跟上..
'''

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canMakeFlower(mid):
            count = 0
            flower = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] < mid:
                    flower +=1
                    if flower == k:
                        count += 1
                        flower = 0
                else:# 不是相邻就直接死掉了
                    flower = 0
            return count >= m

        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = (right - left)//2
            if not canMakeFlower(mid):
                left = mid + 1
            else:
                right = mid
        return mid