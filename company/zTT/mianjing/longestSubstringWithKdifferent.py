from collections import Counter


class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

    def longest_substring_k_distinct(s, k):
        window_start = 0
        max_length = 0
        char_frequency = {}

        for window_end in range(len(s)):
            right_char = s[window_end]
            char_frequency[right_char] = char_frequency.get(right_char, 0) + 1

            while len(char_frequency) > k:
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length

    s = "abcdeffg"
    k = 3

    length = longest_substring_k_distinct(s, k)
    print("Length of the longest substring with at most", k, "distinct characters:", length)
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_cnt = {s[0]: 1}
        res = 1
        left = right = 0
        while right + 1 < len(s):
            right += 1
            char_cnt[s[right]] = char_cnt.get(s[right], 0) + 1
            while len(char_cnt) > 2:
                char_cnt[s[left]] -= 1
                if char_cnt[s[left]] == 0:
                    char_cnt.pop(s[left])
                left += 1

            res = max(res, right - left + 1)

        return res