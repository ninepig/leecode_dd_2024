class Solution:
    # 先从左往右 算出乘以左侧的
    # 在右侧往左,算出乘以右侧的
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1 for _ in range(size)]
        left = 1
        for i in range(size):
            res[i] *= left
            left *= res[i]

        right = 1
        for i in range(size - 1 ,-1,-1):
            res[i] *= right
            right *= res[i]

        return res
