'''
经典滑动指针
python的library 比java省事100倍
'''

import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left , right = 0 , 0
        s1_counter = collections.Counter(s1)
        window_counter = collections.Counter()
        window_size = len(s1)
        while right < len(s2):
            window_counter[s2[right]] += 1

            if right - left + 1 >= window_size:
                if window_counter == s1_counter :
                    return True
                window_counter[s2[left]] -= 1
                if window_counter[s2[left]] == 0 :
                    del window_counter[s2[left]]
                left += 1

            right += 1

        return False