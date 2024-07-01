'''
这道题是桶 或者 slidingwindows 两种做法
桶排序非常优雅
也是经典桶排序的题
'''
import bisect
from typing import List

from sortedcontainers import SortedList


## 这个题太牛逼了。。

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket_list = dict()
        for i in range(len(nums)):
            bucket_index = nums[i] // (t + 1) ## bucket index
            if bucket_index in bucket_list: # this bucket already exist
                return True
            ## check if left bucket exist and value is smaller than t
            if bucket_index - 1 in bucket_list and abs(nums[bucket_index - 1] - nums[i]) <= t:
                return True
            ## check right
            if bucket_index + 1 in bucket_list and abs(nums[bucket_index + 1] - nums[i]) <= t:
                return True

            ## pop bucket which distance is bigger than k
            if i >= k:
                bucket_list.pop(nums[i-k] // (t + 1))

        return False


class SolutionSw:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        size = len(nums)
        window = SortedList()
        left, right = 0, 0
        while right < size:
            window.add(nums[right])

            if right - left > k:
                window.remove(nums[left])
                left += 1

            idx = bisect.bisect_left(window, nums[right])

            if idx > 0 and abs(window[idx] - window[idx - 1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx + 1] - window[idx]) <= t:
                return True

            right += 1

        return False