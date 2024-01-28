'''
Given a list of employee work schedules with each employee having a list of non-overlapping intervals representing their working hours, we are tasked with finding the common free time for all employees, or in other words, the times when all employees are not working.

The input is a nested list of intervals, each interval as [start, end], with start < end. The intervals are non-overlapping and are already sorted in ascending order. The output should also be a list of sorted intervals.

For example, consider schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]. Here, Employee 1 works from 1 to 3 and 6 to 7. Employee 2 works from 2 to 4 and Employee 3 works from 2 to 5 and 9 to 12. The common free time for all employees is [5,6] and [7,9] as these are the intervals when all employees are free.

有点类似于会议室
就是 input 不一样
'''


#python
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        inteveral = []
        ## form a big interval list
        for employee in schedule:
            for item in employee:
                inteveral.append(item)

        inteveral.sort(key = lambda x: x[0]) # sort by starting time

        res = []
        end = inteveral[0][1] # found first end time

        for i in range(1,len(inteveral)):
            if end < inteveral[i][0] :# if we found intveral, only when end smaller than next start
                res.append([end,inteveral[i][0]])
            end = max(end,inteveral[i][1]) # found bigger end value

        return res

