class Solution:
    #  If not, return the index where it would be if it were inserted in order.
    # 这道题还是直接取值法, 因为找到目标位置,如果不存在 直接返回left 即可. 此时left == right 就是正确位置
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left , right = 0, size - 1
        while left <= right :
            mid = left + (right - left )//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                right = mid + 1
            else:
                left = mid - 1

        return left 
