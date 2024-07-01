## 这个题是二分法的应用题
## 如果mid < mid +1  就往右侧找
## 如果 mid > mid +1 就往左侧找
## 最终left == right的时候退出循环
## 这样一定能有left 》 right 肯定是峰值
## 162和852 一模一样
class Solution:
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
