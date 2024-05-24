class Solution:
    # 349 Given two integer arrays nums1 and nums2,
    # return an array of their intersection.
    # Each element in the result must be unique and you may return the result in any order.
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hashset should be easiest way
        helpSet = set()
        helpSet2 = set()
        res = []
        for num in nums1:
            helpSet.add(num)

        for num in nums2:
            helpSet2.add(num)

        for val in helpSet2:
            if val in helpSet:
                res.append(val)

        return res
        #
        # """
        #   :type nums1: List[int]
        #   :type nums2: List[int]
        #   :rtype: List[int]
        #   """
        # return list(set(nums1) & set(nums2))
    # one dict
    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i] + 1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0

        return res
    ## two pointer with sorting
    def intersection3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if not (len(res) and nums1[i] == res[len(res) - 1]):
                    res.append(nums1[i])
                i += 1
                j += 1

        return res



    ## 350,Given two integer arrays nums1 and nums2, return an array of their intersection.
    # Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



    class Solution:
        def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
            d = {}
            for i in nums1:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
            list1 = []
            for i in nums2:
                if i in d and d[i] > 0:
                    list1.append(i)
                    d[i] -= 1
            return list1

    class Solution:
        def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

            nums1.sort()
            nums2.sort()

            one = 0
            two = 0

            ans = []

            while one < len(nums1) and two < len(nums2):

                if nums1[one] < nums2[two]:
                    one += 1
                elif nums2[two] < nums1[one]:
                    two += 1
                else:
                    ans.append(nums1[one])
                    one += 1
                    two += 1
            return ans