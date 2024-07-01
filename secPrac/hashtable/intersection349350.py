import collections


class Solution:
    '''
    给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序
    '''
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_set = set(nums1)
        res_set = []

        for num in nums2:
            if num in num1_set:
                res_set.append(num)

        return set(res_set)

    '''给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。
    返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。
    可以不考虑输出结果的顺序
    '''
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        num1_counter = collections.counter(nums1)
        for num in nums2:
            if num in num1_counter:
                if num1_counter[num] > 0:
                    res.append(num)
                    num1_counter[num] -= 1

        return res