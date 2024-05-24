import collections

'''经典题
类似643
但一个是anagram
一个是不固定string
一个fix 一个no-ifx windows'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultDict(int)
        window = collections.defaultdict(int)
        for ch in t:
            need[ch] += 1

        left , right = 0 , 0
        valid = 0
        start = 0
        size = len(s) + 1

        while right < len(s):
            cur_char = s[right]
            right += 1

            if cur_char in need :
                window[cur_char] += 1
                if window[cur_char] == need[cur_char]:
                    valid += 1

            while valid == len(need):
                if right - left < size:
                    start = left
                    size = right - left

                remove_ch = s[left]
                left += 1

                if remove_ch in need:
                    if window[remove_ch] == need[remove_ch]:
                        valid -= 1
                    window[remove_ch] -= 1

        if size == len(s) + 1:
            return  ''

        return  s[start : start + size]
