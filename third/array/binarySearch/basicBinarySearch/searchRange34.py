## 第一个 以及最后一个， 所以要用逼近得做法，也就是排除法
## 同时要用 left < right 这个判断条件
## 非常标准的逼近，
## left = mid + 1 ---> mid = left(right - left) //2 是一起出现的
## right = mid + 1 ---> mid = left(right - left +1）//2 是一起出现的
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ## santity check
        left , right = 0 , len(nums) - 1
        ans= [-1,-1]
        ## 找到第一个比 target小的值，逼近
        while left < right:
            mid = left + (right - left) //2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return ans
        ans[0] = left

        left , right = 0, len(nums) -1
        ## 找到第一个比target 大的值， 逼近
        while left< right:
            mid = left + (right -left + 1)//2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        if nums[left] == target:
            ans[1] = left

        return ans
