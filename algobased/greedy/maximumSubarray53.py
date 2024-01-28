class Solution:
    '''贪心的思维,对于当前值,我们只看之前是否大于0, 小于0 就没有意义了'''
    def maxSubArray(self, nums: List[int]) -> int:
        local = nums[0]
        max_sum = nums[0]
        size = len(nums)
        for i in range(1,size):
            if local < 0: # if local smaller than 0 , we dont want that any more
                local = nums[i]
            else:
                local += nums[i] #can try current nums[i]
            max_sum = max(local,max_sum)

        return max_sum