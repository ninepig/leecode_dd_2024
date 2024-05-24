class Solution:
    '''
    定义状态 dp[i]表示为：将正整数
   拆分为至少 2个正整数的和之后，这些正整数的最大乘积
   0 1 不能拆分 dp[0] dp[1] = 0
   状态转移 dp[i] = max( 不能拆分的情况 (i-j)*i  拆分 dp[i-j] * j)
    '''
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max((i - j) * j, dp[i - j] * j)
        return dp[n]