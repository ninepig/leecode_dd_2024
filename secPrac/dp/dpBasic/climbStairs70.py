class Solution:
    def climbStairs(self, n: int) -> int:
        # 和 fib 是一模一样的写法
        # dp[n] reach n stairs -> how many method
        # dp[0] = 0 dp[1] = 1
        # transfer => dp[n] = dp[n-1] + dp[n-2]
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i - 2]

        return dp[n]

