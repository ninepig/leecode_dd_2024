class Solution:
    '''basic binary search'''
    # LOG(N)
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        size = len(nums)
        left = 0
        right = size - 1

        # 直接法， 如果找不到 直接返回-1 ，因为已经全部搜索了整个数组
        while left <= right:
            mid = left + (right - left ) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
