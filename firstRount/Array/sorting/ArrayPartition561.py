'''
脑筋类题目

要想每对数最小值的总和最大，就得使每对数的最小值尽可能大。只有让较大的数与较大的数一起组合，较小的数与较小的数一起结合，才能才能使总和最大。

对 nums 进行排序。
将相邻两个元素的最小值进行相加，即得到结果
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])