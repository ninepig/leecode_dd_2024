class Solution:
    '''最简单的贪心法'''
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        s_index = 0
        g_index = 0
        for i in range(len(s)):
            if s[s_index] >= g[g_index]:
                s_index += 1
                g_index += 1
                ans += 1
            else:
                s_index += 1

        return ans

