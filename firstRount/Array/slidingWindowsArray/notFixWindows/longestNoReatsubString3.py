class Solution:
    '''经典'''
    def lengthOfLongestSubstring(self, s: str) -> int:
        windows_dict = dict()
        left , right = 0 , 0
        ans = -1

        while right < len(s):
            if s[right] not in windows_dict:
                windows_dict[s[right]] = 1
            else:
                windows_dict[s[right]] += 1

            while windows_dict[s[right]] > 0 :
                windows_dict[s[left]] -= 1
                left += 1

            ans = max(ans, right -left + 1)
            right += 1

        return  ans