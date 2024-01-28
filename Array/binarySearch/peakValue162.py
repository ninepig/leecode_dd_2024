'''
二分法应用
关键是核心判断条件怎么构成
'''

class Solution:
    '''找到左侧第一个 这个题的核心'''
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


class Solution:

    ''' 1095
    找到index，因为这个只可能存在一个 满足题意'''
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


'''
因为题目要求不能对 MountainArray.get 发起超过 100 次调用。所以遍历数组进行查找是不可行的。

根据山脉数组的性质，我们可以把山脉数组分为两部分：「前半部分的升序数组」和「后半部分的降序数组」。在有序数组中查找目标值可以使用二分查找来减少查找次数。

而山脉的峰顶元素索引也可以通过二分查找来做。所以这道题我们可以分为三步：

通过二分查找找到山脉数组的峰顶元素索引。
通过二分查找在前半部分的升序数组中查找目标元素。
通过二分查找在后半部分的降序数组中查找目标元素。
最后，通过对查找结果的判断来输出最终答案。
'''
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def binarySearchPeak(self, mountain_arr) -> int:
        left, right = 0, mountain_arr.length() - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        return left

    def binarySearchAscending(self, mountain_arr, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid
        return left if mountain_arr.get(left) == target else -1

    def binarySearchDescending(self, mountain_arr, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                right = mid
        return left if mountain_arr.get(left) == target else -1

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()
        peek_i = self.binarySearchPeak(mountain_arr)

        res_left = self.binarySearchAscending(mountain_arr, 0, peek_i, target)
        res_right = self.binarySearchDescending(mountain_arr, peek_i + 1, size - 1, target)

        return res_left if res_left != -1 else res_right