# https://www.fastprep.io/problems/find-median-of-subarray-uniqueness
# In an Amazon coding marathon, the following challenge was given.
#
# The uniqueness of an array of integers is defined as the number of distinct elements present. For example, the uniqueness of [1, 5, 2, 1, 3, 5] is 4, element values 1, 2, 3, and 5. For an array arr of n integers, the uniqueness values of its subarrays is generated and stored in another array, call it subarray_uniqueness for discussion. Find the median of the generated array subarray_uniqueness.
#
# Notes:
#
# The median of a list is defined as the middle value of the list when it is sorted in non-decreasing order. If there are multiple choices for median, the smaller of the two values is taken. For example, the median of [1, 5, 8] is 5, and of [2, 3, 7, 11] is 3.
# A subarray is a contiguous part of the array. For example, [1, 2, 3] is a subarray of [6, 1, 2, 3, 5] but [6, 2] is not.
# Function Description
#
# Complete the function findMedianOfSubarrayUniqueness in the editor.
#
# findMedianOfSubarrayUniqueness has the following parameter:

# class Solution:
#   def findMedianOfSubarrayUniqueness(self, arr: List[int]) -> int:
#     unique = []
#     head = 0
#     for i in range(len(arr)):
#         filter = set()
#         subarr = arr[head:head+i]
#         for num in subarr:
#             filter.add(num)
#         unique.append(len(filter))
#     return unique[int(len(unique)/2)]


from typing import List
from collections import defaultdict

array =[1, 2, 1]

# array = [1, 2, 3, 4, 5, 6]

# arr = [1, 2, 1]

## This func returns the number of subarrays that have at most k distinct elements
def atMostDistinct(k: int) -> int:
    counter = 0

    hMap = defaultdict(int)
    l, r = 0, 0

    while r < len(array):
        hMap[array[r]] += 1

        # Shrink window if > k
        while len(hMap) > k:
            hMap[array[l]] -= 1
            if hMap[array[l]] == 0:
                del hMap[array[l]]
            l += 1

        counter += (r - l) + 1
        r += 1

    return counter


def findMedianOfSubarrayUniqueness(arr: List[int]) -> int:
    N = len(arr)
    numberOfSubarrays = (N * (N + 1)) // 2
    medianIndex = (numberOfSubarrays - 1) // 2 if numberOfSubarrays % 2 == 0 else numberOfSubarrays // 2
    maxMedianValue = len(set(array))
    print("")

    ## Binary search between 1 and maxMedianValue
    ## lets say BS between 1 - 5
    ## take 3, if this is median, the result,
    l, r = 1, maxMedianValue

    while l <= r:
        mid = l + (r - l) // 2

        if atMostDistinct(mid - 1) < medianIndex + 1 <= atMostDistinct(mid):
            return mid
        elif medianIndex + 1 <= atMostDistinct(mid - 1):
            r = mid - 1
        else:
            l = mid + 1

    return mid


print(findMedianOfSubarrayUniqueness(array))