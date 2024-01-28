class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        len(num1) is way biggher than nums2
        """
        index_first = m - 1
        index_second = n - 1
        index_write = m + n - 1
        ## write from back to begin to avoid overwrite
        while index_first >= 0 and index_second >=0:
            if nums1[index_first] >= nums2[index_second]:
                nums1[index_write] = nums1[index_first]
                index_first -= 1
                index_write -= 1
            else:
                nums1[index_write] = nums2[index_second]
                index_second -= 1
                index_write -= 1

        # while index_first >= 0:
        #     nums1[index_write] = nums1[index_first]
        #     index_first -= 1
        #     index_write -= 1
        #
        # while index_second >= 0:
        #     nums1[index_write] = nums2[index_second]
        #     index_second -= 1
        #     index_write -= 1

        ## 省略写法。。对应21 -- 29
        nums1[:index_second + 1] = nums2[:index_second + 1]
