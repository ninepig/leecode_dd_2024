class Solution:
    '''这个题就是个变形的 unfix windows 应用题 关键是想明白 没啥难的'''
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        size = len(s)
        costs = [0 for _ in range(size)]
        for i in range(size):
            costs[i] = abs(ord(s[i]) - ord(t[i]))

        left, right = 0, 0
        ans = 0
        window_sum = 0
        while right < size:
            window_sum += costs[right]
            while window_sum > maxCost:
                window_sum -= costs[left]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans