class Solution:
    '''技巧叫做 原地hash'''
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0 :
            return -1
        size = len(nums)
        for i in range(size):
            # keep exchange to make 1 goto num[0], 2 goto num[1]
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                index1 = i
                index2 = nums[i] - 1
                nums[index1] , nums[index2] = nums[index2] , nums[index1]

        for i in range(size):
            if nums[i] != i+ 1:
                return i + 1
        return size + 1