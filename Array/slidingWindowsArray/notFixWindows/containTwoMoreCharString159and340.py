'''
比较直接的题
但是作者这个 if 的条件 多次出现了
如果if 怎么样 。
其实用while 应该也可以
'''
import collections
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_count = 0
        k = 2
        counts = collections.defaultdict(int)
        count = 0
        left, right = 0, 0
        while right < len(s):
            if counts[s[right]] == 0:
                count += 1
            counts[s[right]] += 1
            right += 1
            if count > k:
                if counts[s[left]] == 1:
                    count -= 1
                counts[s[left]] -= 1
                left += 1
            max_count = max(max_count, right - left)
        return max_count

    # 和上面呼应了 一个 while 一个不用while 我觉得下面这种更直观
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = 0
        window_counts = dict()
        left, right = 0, 0

        while right < len(s):
            if s[right] in window_counts:
                window_counts[s[right]] += 1
            else:
                window_counts[s[right]] = 1

            while (len(window_counts) > k):
                window_counts[s[left]] -= 1
                if window_counts[s[left]] == 0:
                    del window_counts[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans