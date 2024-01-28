from typing import List

'''
将两个指针 index1、index2 分别指向 nums1、nums2 数组的尾部，再用一个指针 index 指向数组 nums1 的尾部。
从后向前判断当前指针下 nums1[index1] 和 nums[index2] 的值大小，将较大值存入 num1[index] 中，然后继续向前遍历。
最后再将 nums2 中剩余元素赋值到 num1 前面对应位置上
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index1 = m - 1
        index2 = n - 1
        index = m + n -1
        while index2 >= 0 and index1 >= 0:
            if nums2[index2] >= nums1[index1]:
                nums1[index] = nums2[index2]
                index2 -= 1
            else:
                nums1[index] = nums1[index1]
                index1 -=1
            index -= 1
        # 很巧妙的方法
        nums1[:index2 + 1] = nums2[:index2 + 1]