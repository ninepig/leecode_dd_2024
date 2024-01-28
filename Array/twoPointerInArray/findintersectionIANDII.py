'''
经典双指针

'''
'''
同样的就加入结果
双指针即可
重复元素只计算一次
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        left_1 = 0
        left_2 = 0
        res = []
        while left_1 < len(nums1) and left_2 < len(nums2):
            if nums1[left_1] == nums2[left_2]:
                if nums1[left_1] not in res:
                    res.append(nums1[left_1])
                left_1 += 1
                left_2 += 1
            elif nums1[left_1] < nums2[left_2]:
                left_1 += 1
            elif nums1[left_1] > nums2[left_2]:
                left_2 += 1
        return res

'''
350
需要计算出现的次数
'''
        def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
            numDict = dict()
            nums = []
            for num in nums1:
                if num in numDict:
                    numDict[num] += 1
                else:
                    numDict[num] = 1
            for num in nums2:
                if num in numDict and numDict[num] != 0:
                    numDict[num] -= 1
                    nums.append(num)
            return nums