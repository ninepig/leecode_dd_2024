'''
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## 单调栈， next bigger element‘s index - current vaule's index
        ## using a stack to record element ,index , when we pop value, it's(poped item) next bigger one is the current value
        if not temperatures or len(temperatures) == 0:
            return [0]
        stack = []
        length = len(temperatures)
        res = [0] * length
        for i,v in enumerate(temperatures):
            ## mono increasing stack
            while stack and temperatures[stack[-1]] < v:
                top_index = stack.pop()
                res[top_index] = i - top_index
            stack.append(i)

        return res

sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(sol.dailyTemperatures(temperatures))