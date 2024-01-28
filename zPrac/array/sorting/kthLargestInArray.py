import heapq
from random import random


class Solution:
    '''
    1 sort
    2 heap
    3 quick sort
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap,num)
            else:
                if minheap[0] < num: # 栈顶元素小于当前元素,需要出栈, 因为要维护k个最大的值 栈顶即可第k大
                    heapq.heappop(minheap)
                    heapq.heappush(minheap,num)

        return minheap[0]

    def findKthLargestQuickSort(self, nums: List[int], k: int) -> int:
        return self.quickSort(nums,0,len(nums) - 1, k,len(nums))

    # def quickSort(self, nums, start, end, k, size):
    #     if start < end:
    #         pivot = self.randomPartition(start,end,nums)
    #         if pivot == size - k:
    #             return nums[size - k]
    #         if pivot < size - k :
    #             self.quickSort(nums,0,pivot - 1 , k , size)
    #         if pivot > size - k:
    #             self.quickSort(nums,pivot + 1 , end, k , size)
    #
    #     return nums[size - k]
    #
    # def randomPartition(self, start, end, nums):
    #     i = random.randint(start,end)
    #     nums[i],nums[start] = nums[start],nums[i] # put random pivot to low pos
    #
    #     return self.partition(nums, start, end)
    #
    # def partition(self, nums, start, end):
    #     pivot = nums[start]
    #
    #     i , j = start, end
    #
    #     while i < j :
    #         while i < j and nums[j] >= pivot:# find first element smaller than pivot from right
    #             j -= 1
    #         while i < j and nums[i]<= pivot: # find first element bigger than pivot on left
    #             i += 1
    #         nums[i],nums[j] = nums[j], nums[i]
    #
    #     nums[j] , nums[start] = nums[start] , nums[j] # put pivot to it pos
    #
    #     return j # return pivot
    def quickSort(self, nums, low, high, k, size):
        if low < high:
            pivot = self.randomPartition(nums,low,high)
            if pivot == size - k: # we found
                return nums[size - k]
            elif pivot < size - k:
                self.quickSort(nums,low,pivot - 1 , k , size)
            else:
                self.quickSort(nums,pivot + 1 , high, k, size)

        return nums[size - k ]

    def randomPartition(self, nums, low, high):
        pivot = random.randomInt(low,high)
        nums[low],nums[pivot] = nums[pivot],nums[low]

        return self.partition(nums,low,high)

    def partition(self, nums, low, high):
        pivot = nums[low]
        i , j = low, high
        while i < j:
            while i < j and nums[j] >= pivot :
                j -= 1
            while i < j and nums[i] <= pivot :
                i += 1
            nums[i],nums[j] = nums[j],nums[i]

        nums[j] , nums[low] = nums[low] , nums[j]
        return j







