class Solution:
    '''
    basic binary search
    '''
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) - 1
        while left < right : ## 用 《= 就不需要再判断了
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left if nums[left] == target else -1
