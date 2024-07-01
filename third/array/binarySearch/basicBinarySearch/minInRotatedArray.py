'''
二分逼近法
1 画图， 因为是rotate
num[right]是最右侧值， 这个是这道题的核心
肯定要比左侧大
我们拿中间值和右侧比
如果 num[mid] > num[right] 则表示 最小值一定在mid右侧  mid = left + 1
如果 num[mid]<= num[right] 则表示 最小值一定再mid左侧或者是mid
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left ) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

'''
如果有重复元素
我们就会出现 num[mid] == num[right]的情况

'''
class SolutionDuplicated:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                ##当出现dup的情况下 我们无法判断两侧，只能将最大值减小，这样用于逼近
                right = right - 1
        return nums[left]
