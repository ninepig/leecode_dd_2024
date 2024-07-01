import collections

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        windows_coutner = collections.Counter()
        left = 0
        right = 0
        res = 0
        while right < len(s):
            windows_coutner[s[right]] += 1
            if right - left + 1 >= k:
                if len(windows_coutner) == k:#如果没有重复， 就说明counter的size 和k 一样。。这个小技巧学习到了
                    res+=1
                windows_coutner[s[left]] -=1
                if windows_coutner[s[left]] == 0:
                    del windows_coutner[s[left]]
                left += 1
            right += 1
        return res