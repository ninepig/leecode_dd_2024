'''
本质也是一个贪心。
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 经典题，画图 2种情况 1重叠 2 不重叠
        intervals.sort(key=lambda x:x[0])
        res = []
        for interval in intervals:
            # not overlap or res is empty
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1],interval[1])

        return res