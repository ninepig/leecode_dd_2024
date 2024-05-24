#https://leetcode.cn/problems/trapping-rain-water/solutions/9112/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/

class Solution:
    '''单调栈的优势就是找左边比当前大的 右边比当前大的。 来计算 面积。 画图就知道了
    当然这个题更多别的方法。二刷的时候多搞搞'''
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        size = len(height)

        for i in range(size):
            # find left , right and calc
            while stack and height[i] > stack[-1]:
                #注意 是pop， 所以left 是pop以后的stack
                cur = stack.pop(-1)
                # if we can find left side height
                if stack :
                    #  左移 右移 用来计算面积
                    left = stack[-1] + 1
                    right = i - 1
                    high = min(height[i], stack[-1]) - height(cur)
                    res += high *(right - left + 1)  # index + 1
                else:
                    break
            stack.append(i)

        return res