class Solution:
    # 原地hash, 把元素放到 i - 1 的位置上, 比如元素1 放到位置0上 元素2 放到位置1 上
    # 和 missing postive 一样
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while 1<= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                index1 = i
                index2 = nums[i] - 1
                nums[index1] , nums[index2] = nums[index2] , nums[index1]

        res = []
        for idx, value in enumerate(nums):
            if idx != value:
                res.append(value)

        return res
