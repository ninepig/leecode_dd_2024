class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = dict()
        for num in nums:
            if num in hset:
                return True
            #dict 的用法 python  毕竟是个2维数组
            hset[num] = num
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def containsDuplicate3(self, nums: List[int]) -> bool:
        #python sort 的用法
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False