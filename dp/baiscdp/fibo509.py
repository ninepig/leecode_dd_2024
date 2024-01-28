class Solution:
    '''
    1split phase
    2define state
    3 state transfer
    4 inital state
    5 final state
    '''
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        # split phase, 把fib数 放到 n + 1个数组之中 , dp[i] means state
        dp = [0 for i in range(n+1)]

        # initial state
        dp[0] = 0
        dp[1] = 1

        # state transfer
        for i in range(2,n + 1):
            dp[i] = dp[i-2] + dp[i-1]

        # final state
        return dp[n]


'''自顶而下'''
class SolutionTopDown:
    def fib(self, n: int) -> int:
        # 使用数组保存已经求解过的 f(k) 的结果
        memo = [0 for _ in range(n + 1)]
        return self.my_fib(n, memo)

    def my_fib(self, n: int, memo: List[int]) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        # 已经计算过结果
        if memo[n] != 0:
            return memo[n]

        # 没有计算过结果
        memo[n] = self.my_fib(n - 1, memo) + self.my_fib(n - 2, memo)
        return memo[n]