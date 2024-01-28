class Solution:
    '''滑动数组, 替换k以后最长的重复序列'''
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = float('inf')
        left , right = 0, 0
        ans = 0
        count = [0 for _ in range(26)]
        while right < len(s):
            char_right = ord(s[right]) - ord('A')
            count[char_right] += 1
            max_count = max(max_count,count[char_right])
            while right - left + 1 > max_count + k :# k is not enough for change to all same char
                char_left = ord(s[left]) - ord('A')
                count[char_left] -= 1
                left += 1

            ans = max(ans,right - left + 1)
            right += 1

        return ans
