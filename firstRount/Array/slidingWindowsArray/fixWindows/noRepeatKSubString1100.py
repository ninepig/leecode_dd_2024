import collections

'''
python collection
string + sliding windows 
'''
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        left, right = 0, 0
        window_count = collections.Counter()
        ans = 0

        while right < len(s):
            window_count[s[right]] += 1

            if right - left + 1 >= k:
                if len(window_count) == k:
                    ans += 1
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1

            right += 1

        return ans
