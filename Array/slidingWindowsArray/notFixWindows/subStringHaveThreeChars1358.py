class Solution:
    '''基本的题 但是这道题的关键是
    、ans += len(s) - right
    对于这个windows 他可以组成的subString是他到windows尾部还有的个数 的组合
    理解这个就明白了 非常好的做法'''
    def numberOfSubstrings(self, s: str) -> int:
        window = dict()
        ans = 0
        left, right = 0, 0

        while right < len(s):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

            while len(window) >= 3:
                ans += len(s) - right
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            right += 1
        return ans