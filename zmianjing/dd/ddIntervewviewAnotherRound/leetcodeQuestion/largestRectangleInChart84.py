class Solution:
    # brutal force way
    def largestRectangleArea(self, heights: list[int]) -> int:
        res = 0
        for i in len(heights):
            cur_height = heights[i]
            left_index = i
            right_index = i
            while left_index > 0 and heights[left_index] >= cur_height:
                left_index -= 1
            # 细节
            while right_index < len(heights) - 1 and heights[right_index] >= cur_height:
                right_index += 1

            max_width = right_index - left_index + 1
            res = max(res,max_width*cur_height)

        return res

    ## monotonoic stack
    # brutal force way
    def largestRectangleAreaStack(self, heights: list[int]) -> int:
        ans = 0
        stack = []
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