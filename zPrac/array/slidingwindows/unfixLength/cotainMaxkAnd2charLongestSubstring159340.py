import collections
'''
这两道题体现了defaultdict的优缺点
一个可以用count来做
一个可以用del key来做 (dict, not defaultDict)
因为defaultDict 默认含有0
所以len(map)会一直保存含有0的长度

'''
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        windwos = collections.defaultdict()
        left , right = 0,0
        ans = 0
        count = 0
        while right < len(s):
            right_char = s[right]
            if windwos[right_char] == 0:
                count += 1 # only we dont have right char in complexDs, we add 1
            windwos[right_char] += 1

            while count > 2 :
                left_char = s[left]
                windwos[left_char] -= 1
                if windwos[left_char] == 0:
                    count -=1
                left += 1

            # logic
            ans = max(ans,right - left + 1)

            right += 1

        return ans

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