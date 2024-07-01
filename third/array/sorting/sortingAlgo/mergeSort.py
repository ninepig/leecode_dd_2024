'''

https://algo.itcharge.cn/01.Array/02.Array-Sort/05.Array-Merge-Sort/#_3-%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F%E4%BB%A3%E7%A0%81%E5%AE%9E%E7%8E%B0

树的后序就是基于merge sort
先拆 再合并
'''


class Solution:
    # 合并过程
    def merge(self, left_nums: [int], right_nums: [int]):
        nums = []
        left_i, right_i = 0, 0
        while left_i < len(left_nums) and right_i < len(right_nums):
            # 将两个有序子数组中较小元素依次插入到结果数组中
            if left_nums[left_i] < right_nums[right_i]:
                nums.append(left_nums[left_i])
                left_i += 1
            else:
                nums.append(right_nums[right_i])
                right_i += 1

        # 如果左子数组有剩余元素，则将其插入到结果数组中
        while left_i < len(left_nums):
            nums.append(left_nums[left_i])
            left_i += 1

        # 如果右子数组有剩余元素，则将其插入到结果数组中
        while right_i < len(right_nums):
            nums.append(right_nums[right_i])
            right_i += 1

        # 返回合并后的结果数组
        return nums

    # 分解过程
    def mergeSort(self, nums: [int]) -> [int]:
        # 数组元素个数小于等于 1 时，直接返回原数组
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2  # 将数组从中间位置分为左右两个数组
        left_nums = self.mergeSort(nums[0: mid])  # 递归将左子数组进行分解和排序
        right_nums = self.mergeSort(nums[mid:])  # 递归将右子数组进行分解和排序
        return self.merge(left_nums, right_nums)  # 把当前数组组中有序子数组逐层向上，进行两两合并

    def sortArray(self, nums: [int]) -> [int]:
        return self.mergeSort(nums)
