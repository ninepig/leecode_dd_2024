'''
递减栈 这道题 对于当前柱子 找到左侧比自己小的，找到右侧比自己小的
https://i.loli.net/2018/10/29/5bd65b33c2798.png
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        ans = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                #注意 是pop， 所以left 是pop以后的stack
                cur = stack.pop()
                left = stack[-1] + 1 if stack else 0
                right = i - 1
                ans = max(ans, (right - left + 1) * heights[cur])
            stack.append(i)

        return ans