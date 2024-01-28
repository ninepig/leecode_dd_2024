class Solution:
    '''
    滑动数组
    统计subarray 数量
    '''
    def numberOfSubstrings(self, s: str) -> int:
        windows = dict()
        left, right = 0 ,  0
        ans = 0
        while right < len(s):
            if windows[s[right]] not in s:
                windows[s[right]] = 0
            else:
                windows[s[right]] += 1

            while len(windows) >= 3:
                # cal the ans
                ans += (right - left + 1)

                windows[s[left]] -= 1
                if windows[s[left]] == 0:
                    del windows[s[left]]
                    left += 1

            right += 1

        return ans
