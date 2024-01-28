'''
描述：给定一个大小为
 的数组 nums。

要求：返回其中相同元素个数最多的元素。

思路1
sort， 取中间值， 因为是大部分。 所以必须是在中间的那个数

思路2
hashmap， 取hashmap值最大的

思路3
新算法Moore Voting Algorithm

'''

class Solution:
    def majorityElementSort(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElementHashMap(self, nums: List[int]) -> int:
        numDict = dict()
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1

        maxSize = len(nums) // 2

        for key, val in numDict.items():
            if val > maxSize:
                return key

        return 0

    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate