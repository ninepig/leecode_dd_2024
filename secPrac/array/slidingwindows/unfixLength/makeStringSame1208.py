class Solution:
    '''基本的unfix 滑动数组题, 关键是转化这一步'''
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [0 for _ in range(len(s))]
        for i in range(len(s)):
            cost[i] = abs(ord(s[i]) - ord(t[i]))

        left , right = 0 , 0
        windows_cost = 0
        ans = 0
        while right < len(s):
            windows_cost += cost[right]

            while windows_cost > maxCost:
                windows_cost -= cost[left]
                left += 1

            ans = max(ans, right - left + 1)

            right += 1

        return ans