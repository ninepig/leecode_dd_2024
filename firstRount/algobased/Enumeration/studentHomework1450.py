from firstRount.LinkedList import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        size = len(startTime)
        for i in range(size):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count


    ##这道题应该用的是树状数组/线段树 , 明显的区间查询题 TODO