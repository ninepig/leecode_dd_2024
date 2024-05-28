## leetcode 84
## 最经典的题， 这个用单调递减栈 对于栈顶元素， 他右侧比它小的是 当前value ， 他左侧比它小的是栈顶元素下一个元素。
## 利用两侧栈 来做

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        if not heights or len(heights) == 0 : return 0
        heights.append(0) ## avoid no smaller  on right side.
        ans = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]: ## mono tonic decreasing stack
                cur = stack.pop(-1) ## we cal the cur value's largest
                left = stack[-1] + 1 if stack else  0 ## +1 means right side
                right = i -1 ##  means left side
                ans = max(ans, (right - left + 1) * heights[cur])
            stack.append(i)

        return ans