class Solution:
    ''' 这道题简化一下 就是选择波峰 和波谷, 记录下来
    然后利用贪心的原则 只对当前点选择 要么是波峰 要么是波谷'''
    def wiggleMaxLength(self, nums: List[int]) -> int:
        cur_diff = 0
        pre_diff = 0
        size = 1
        for i in range(len(nums) - 1):
            cur_diff = nums[i + 1] - nums[i]
            if (cur_diff > 0 and pre_diff <= 0) or (cur_diff < 0 and pre_diff >= 0):
                size += 1
                pre_diff = cur_diff

        return size