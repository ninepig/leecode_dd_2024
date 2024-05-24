class Solution:
    '''
    926
    '''
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        f = [0] * (n+1) # monotone increasing ending with 0
        g = [0] * (n+1) # monotine increasing ending with 1
        for i in range(1, n+1):
            if s[i-1] == "1":
                f[i] = f[i-1] + 1
                g[i] = min(f[i-1], g[i-1])
            else:
                f[i] = f[i-1]
                g[i] = min(f[i-1], g[i-1]) + 1

        return min(f[n], g[n])