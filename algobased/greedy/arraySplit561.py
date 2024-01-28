class Solution:
    '''这道题 就是看起来唬人.其实很简单.
    就是基本的贪心
    因为22相加,最小值的最大和 , 所以一定要尽量避免大的数被miss掉,所以排序以后22相取'''
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
    