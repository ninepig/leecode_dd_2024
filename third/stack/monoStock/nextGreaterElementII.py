'''
给定一个循环数组 nums（最后一个元素的下一个元素是数组的第一个元素）。

要求：输出每个元素的下一个更大元素。如果不存在，则输出 -1。

数字 x 的下一个更大的元素：按数组遍历顺序，这个数字之后的第一个比它更大的数。这意味着你应该循环地搜索它的下一个更大的数。
'''

'''
首先这个题是循环数组
---》把数组*2 可以解决
单调栈存储下标即可。
针对下标找到第一个比它大的值 直接更新就行了。不用担心重复数出现的问题。 不像 nextgreateelement1 因为他是去重的，所以不考虑index，只考虑值

https://leetcode.cn/problems/next-greater-element-ii/solutions/638017/dong-hua-jiang-jie-dan-diao-zhan-by-fuxu-4z2g/
'''
class Solution(object):
    def nextGreaterElements(self, nums):
        if not nums or len(nums) == 0 : return []
        length = len(nums)
        res = [-1] * length
        stack = []

        for i in range(length*2):
            while stack and nums[stack[-1]] < nums[i%length]:
                res[stack.pop()] = nums[i%length]
            stack.append(i%length)

        return res

