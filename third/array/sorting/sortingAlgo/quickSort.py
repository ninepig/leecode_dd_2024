'''
快排算法
1 左侧哨兵节点
2 按照哨兵划分 左侧 右侧
3 递归分解

'''
import random


class Solution:
    def sort_Array(self, nums: [int]) -> [int]:
        return self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self,nums:list[int],low,high):
        if low < high:
            pivot = self.random_partition(nums,low,high)
            self.quick_sort(nums,low,pivot - 1)
            self.quick_sort(nums,pivot + 1, high)

    def random_partition(self, nums, low, high):
        random_pivot = random.randint(low,high)
        nums[random_pivot] , nums[low] = nums[low],nums[random_pivot]
        # 以最低位为基准数，然后将数组中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。最后将基准数放到正确位置上
        return self.partition(nums,low,high)

    def partition(self, nums, low, high):
        pivot = nums[low]
        i , j = low, high
        while i < j:
            while i < j and nums[j]>= pivot:
                j -= 1
            while i < j and nums[i] <= pivot:
                i+= 1
            nums[i],nums[j] = nums[j],nums[i]

        ## put pivoot back to it's right pos
        nums[i],nums[low] = nums[low],nums[i]

        return i 