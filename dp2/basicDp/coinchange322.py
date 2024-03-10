class Solution:
    ''' 基本的dp题
     0 定义 dp dp[amount] 是达到amount 的最少的组合数量
     1 base state dp[0] = 0 --》 0元 我们需要0种组合
     2 状态转移 dp[i] = min(dp[i - coin] + 1) , coin can be different input
     3 结果 dp[amount]
     '''
    def coinChange(coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1 )# at least we need amount + 1's length dp
        dp[0] = 0 # basic state
        for i in range(1,amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])

        return -1 if dp[amount] == amount + 1 else dp[amount]