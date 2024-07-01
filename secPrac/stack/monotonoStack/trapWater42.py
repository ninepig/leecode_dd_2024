class Solution:
    # 单调栈,对于每一个格子,找左边最大的,以及右边最大的,然后计算宽度
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[i] > stack[-1]:
                cur_index =stack.pop(-1)
                if stack :
                    cur_left = stack.pop(-1) + 1 # left + 1 means, next element
                    cur_right = i -1
                    ans += (cur_right - cur_left + 1) * height[cur_index]
                else:
                    break
            stack.append(i)

        return ans
