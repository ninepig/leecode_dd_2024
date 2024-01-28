class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        size = len(nums)
        for i in range(size):
            for j in range(i+1 , size):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return[]

    def twoSumDict(self, nums: List[int], target: int) -> List[int]:
        res = []
        helper = dict()
        size = len(nums)
        for i in range(size):
            if helper[target - nums[i]]:
                res.append(i)
                res.append(helper[target - nums[i]])
                break
            helper[nums[i]] = i

        return res