import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needs = collections.DefaultDict()
        windows = collections.DefaultDict()
        size = len(s) - 1 # substring size which contain target subString
        res = ""

        # update needs windows
        for c in t :
            needs[c] += 1

        left = 0
        right = 0
        valid = 0
        start = 0 # missing this in first draft,
        while right < len(s):
            if s[right] in needs:
                windows[s[right]] += 1
                if windows[s[right]] == needs[s[right]]: # same char count
                    valid += 1
            right += 1

            while valid == len(needs): # 满足匹配字符串. 有overlap. 所以更新他的长度.找最小的
                if right - left < size:
                    start = left
                    size = right - left
                remove_ch = s[left]
                left += 1
                if remove_ch in needs:
                    if windows[remove_ch] == needs[remove_ch]:
                        valid -=1
                    windows[remove_ch] -= 1
        if size == len(s) + 1: # does not exist
            return ''

        return s[start: start + size]
                    # new left = right




