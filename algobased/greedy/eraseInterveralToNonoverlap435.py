'''
这道题我们可以转换一下思路。原题要求保证移除区间最少，使得剩下的区间互不重叠。换个角度就是：
「如何使得剩下互不重叠区间的数目最多」。那么答案就变为了：「总区间个数 - 不重叠区间的最多个数」。我们的问题也变成了求所有区间中不重叠区间的最多个数
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # target ---> maximum non overlap inteval
        # greedy
        intervals.sort(key= lambda x:x[1])
        end_pos = intervals[0][1]
        count = 1
        # 对于贪心而言，当前最优解
        for i in range(1,len(intervals)):
            if end_pos < intervals[i][0]:
                count += 1
                end_pos = intervals[i][1]

        return len(intervals) - count
