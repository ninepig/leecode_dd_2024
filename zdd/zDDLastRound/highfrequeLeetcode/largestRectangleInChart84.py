class Solution:
    # brutal force way
    def largestRectangleArea(self, heights: list[int]) -> int:
        n, ans = len(heights), 0
        if n != 0:
            ans = heights[0]
        for i in range(n):
            height = heights[i]
            for j in range(i, n):
                height = min(height, heights[j])
                ans = max(ans, (j - i + 1) * height)
        return ans


    ## monotonoic stack
    def largestRectangleAreaStack(self, heights: list[int]) -> int:
        ans = 0
        stack = []
        ## 这个关键。不能忘了
        heights.append(0) # add one dummy node on right, we will need count rightest one
        ## 单调栈 是针对当前 柱子 找左边第一个比他小的 右边第一个比它小的 这样 就能形成 长方形，因为用的是他的高度来计算。所以相当于找左右边界
        ## 所以用单调递减栈
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]: # monotonic decreasing stack
                cur_index = stack.pop()
                cur_left = stack[-1] + 1 if stack else 0 ## idx + 1  means get the right side of histgram
                cur_right = i - 1 # first smaller on the right side , so highest  should be i - 1 # from right side
                ans = max(ans, heights[cur_index] * (cur_right - cur_left + 1) )
            stack.append(i) # build stack
        return ans