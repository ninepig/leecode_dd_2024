class Solution:
    '''这个题也是做一次就不会忘的'''
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)] # 长度要大于n ，因为要取到n
        for i in range(2,n + 1): # from 2 --> dp[0] = 0 dp[1] = 0, which mean 0 , 1 can not break
            for j in range(i):
                # 状态转移  i 可以拆分成 i - j  （i - j 不能继续拆）
                # i可以拆分成 i - j 可以继续被拆分，所以要在他的dp里寻找
                dp[i] = max(dp[i],dp[i-j]*j,(i-j) * j)
        return dp[n]