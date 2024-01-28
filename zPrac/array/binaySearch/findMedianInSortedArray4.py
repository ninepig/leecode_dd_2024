'''超级经典题'''
class Solution:
#     # bf merge + sort
    def findMedianSortedArraysBF(self, nums1, nums2):
        merge = nums1 + nums2
        merge.sort()
        size = len(merge)

        if size % 2 == 1:
            return float(merge[size//2])
        else:
            left = merge[size//2]
            right = merge[size//2 + 1]
            return float((left + right)//2)

    # 需要细品。。
    def findMedianSortedArrayBinarySearch(self,num1,num2):
        size1 = len(num1)
        size2 = len(num2)
        if size2< size1 :
            self.findMedianSortedArrayBinarySearch(num2,num1) # make sure num1's length is smaller

        total_length = size2 + size1
        left_partition = (total_length + 1)//2
        left, right = 0, size1 ## binary search range

        while left <= right:
            mid = left + (right - left) // 2
            mid2 = left_partition -  mid # how many we got from num2

            l1,l2 , r1, r2 = float('-inf'),float('inf'),float('-inf'),float('inf')
            if mid < size1:
                r1 = num1[mid]
            if mid2 < size2:
                r2 = num2[mid2]
            if mid-1 >= 0:
                l1 = num1[mid - 1]
            if mid2 - 1 >= 0:
                l2 = num2[mid2 - 1]

            # l1 l2  r1 r2 here is the order
            if l1 <= r2 and l2 <= r1: # we found right partition
                if total_length%2 == 1:
                    return max(l1,l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            if l1 > r2: # order l2r2 l1 r1 mid is on right side
                right = mid + 1
            if r1 < l2:
                left = mid - 1

        return -1 # not exsist



