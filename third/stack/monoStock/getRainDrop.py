## 接雨水 42
'''
单调栈
类似84
84是单调递减
对于栈顶 左侧比他小 右侧比他小的

42 是单调递增
对于栈顶，左侧比他大，右侧比他大
但这个要把所有的都loop一次
'''

class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        stack = []
        size = len(height)
        for i in range(size):
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop(-1)
                if stack:
                    left = stack[-1] + 1
                    right = i - 1
                    high = min(height[i], height[stack[-1]]) - height[cur]
                    ans += high * (right - left + 1)
                else:
                    break
            stack.append(i)
        return ans
