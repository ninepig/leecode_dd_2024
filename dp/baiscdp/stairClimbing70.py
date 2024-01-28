class Solution:
    '''
    1split phase
    2define state
    3 state transfer
    4 inital state
    5 final state
    '''
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[n]

