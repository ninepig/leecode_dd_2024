class Solution:
    '''类似第一个正数的 原地hash
    而且保证数组区间是0--n 所以num[index] 不会越界
    因为只能o（n） 外加no more space
    只能用index来标注是否已经出现
    '''
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            num = abs(nums)
            if nums[num-1] < 0:
                res.append(nums)
            else:
                nums[num-1] = -nums[num - 1]

        return res