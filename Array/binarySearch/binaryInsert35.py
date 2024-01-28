class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        #[right + 1, right]，此时待查找区间为空，待查找区间中没有元素存在， 所以左侧就是目标元素，也就是最接近目标的值
        return left