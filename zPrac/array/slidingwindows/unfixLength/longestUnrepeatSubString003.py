class Solution:
    '''滑动数组左滑的条件 理解透彻'''
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        windows_dict = dict()
        ans = 0
        while right < len(s):
            if s[right] not in windows_dict:
                windows_dict[s[right]] = 1
            else:
                windows_dict[s[right]] += 1

            ## windows条件可以这么写..只要value >=2 学习到了滑动数组
            while windows_dict[s[right]] > 1:
                if s[left] in windows_dict:
                    windows_dict[s[left]] -= 1
                    left += 1

            ans = max(right -left + 1 ,ans)
            right += 1

        return ans

