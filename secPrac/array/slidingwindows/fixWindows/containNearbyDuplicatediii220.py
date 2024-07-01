'''
经典老题
abs(num[i] - num[j]) <= t
abs (i - j) <= k
'''
from bisect import bisect

from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        windows = SortedList() # 利用sortedList 来做， 这个很关键。因为在这里可以找到左右相邻的value，便于search
        left , right = 0 , 0
        while right < len(nums):
            windows.add(nums[right])#要用add 不能用append
            if right - left  + 1 >= k: # windows bigger than k, which means windows already arrive target size, we can count
                # handle logic
                pos = bisect.bisect_left(windows,nums[right])
                if pos > 0 and abs(windows[right] - windows[right - 1]) <=t :
                    return True
                if pos < len(windows) - 1 and abs(windows[right] - windows[right + 1]) <=t :
                    return True
                windows.remove(nums[left]) # 要用remove 不能用pop
                left += 1

            right += 1

        return False



