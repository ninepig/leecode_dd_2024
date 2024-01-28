class Solution:
    '''滑动不固定数组 + hashtable 多练习'''
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        char_dict = []
        size = len(s)
        left , right = 0 , 0
        while right < size:
            if s[right] not in char_dict:
                char_dict[s[right]] = 1
            else:
                char_dict[s[right]] += 1

            while char_dict[s[right]] > 0:
                char_dict[s[left]] -= 1
                left += 1

            # 滑动窗口的有效长度
            ans = max(ans, right - left + 1)

            right += 1

        return ans