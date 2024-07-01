class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        windows = dict()
        while right < len(s):
            right_char = s[right]
            if right_char not in windows:
                windows[right_char] = 1
            else:
                windows[right_char] += 1
            #用这个来作为windows shrink的条件.
            while windows[right_char] > 1:
                windows[s[left]] -= 1
                left -= 1

            ans = max(ans, right - left + 1)

            right += 1
        return ans