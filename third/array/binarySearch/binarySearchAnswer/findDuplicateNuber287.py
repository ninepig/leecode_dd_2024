class Solution:
    ## 这个题是很特别的二分法
    '''
    不能使用任何额外空间。 里用二分法来找到中间数的比他大 比它小的 数量
    不断逼近。 非常好的二分法
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1

            if cnt <= mid:
                left = mid + 1
            else:
                right = mid

        return left
