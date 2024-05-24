'''

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

'''
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
         在 num2之中 用单调栈过一次， 把next element 用dict的形式找出来
         然后用num1 的元素过一遍
         ## 没有重复的元素，所以可以。要不然就是要用list
        '''
        ## santity check
        if not nums1 or not nums2: return []
        next_greater = dict()
        stack = []
        for i , v in enumerate(nums2):
            while stack and stack[-1] < v:
                next_greater[stack[-1]] = v
                stack.pop()
            stack.append(v)
        res = []
        for num in nums1:
            res.append(next_greater.get(num,-1))

        return res
    

