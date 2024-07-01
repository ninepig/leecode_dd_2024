import math
from cmath import inf


class Solution:
    '''
    dp[i] 表示通过复制黏贴---》i个字符 需要最少操作
    dp[i] ===> dp[i/j] + j , dp[i] , dp[j] + i/j
    我们枚举 i的因子，从中找到满足j 能够整除i的条件下， 最小的dp[j] + i/j 即为dp[i] --> 同理 dp[i/j] + j
    '''
    def minSteps(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(2,n+1):
            dp[i] = inf
            for j in range(1,int(math.sqrt(n)) + 1):# 优化， 因为sqt 就够了， 减少循环
                if i % j == 0:
                    dp[i] = min(dp[i], dp[i/j] + j , dp[j] + i )

        return dp[n]
