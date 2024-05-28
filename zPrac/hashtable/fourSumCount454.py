class Solution:
    # brutal force, n4
    # complexDs n2
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sumMap = dict()
        for num in nums1:
            for num2 in nums2:
                sum = num + num2
                if sum in sumMap:
                    sumMap[sum] += 1
                else:
                    sumMap[sum] = 1

        count = 0
        for num in nums3:
            for num2 in nums4:
                sum = num + num2
                if -sum in sumMap:
                    count+= sumMap[-sum] # 全部加上即可

        return count