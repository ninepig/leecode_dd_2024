class Solution:
    '''简单题'''
    def missingNumber(self, nums: List[int]) -> int:
        hash_set = set(nums)
        for num in range(len(nums) + 1):
            if num not in hash_set:
                return num

        return -1


    '''数学'''
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        n = len(nums)
        return (n+1)*n//2 - sum_nums