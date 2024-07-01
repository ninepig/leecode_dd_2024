from functools import cache


class Solution:
    '''最基本的dp题
    dp[0] = 0
    dp[1] = 1
    dp[n] = dp[n-1]+dp[n-2]'''
    def fib(self, n: int) -> int:
        # dfs + mem
        @cache
        def dfs(n):
            if n == 0 :
                return 0
            if n == 1:
                return 1

            return dfs(n - 1) + dfs(n - 2)

        return dfs(n)

    def fib(self, n: int) -> int:
        if n <= 1: return n
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


