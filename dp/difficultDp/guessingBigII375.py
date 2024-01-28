class Solution:
    '''
    https://medium.com/@USTCLink/%E5%92%8C%E6%88%91%E4%B8%80%E8%B5%B7%E5%88%B7leetcode-375-guess-number-higher-or-lower-ii-29b3ded9963d
    答案都看不大明白..真的太菜了
    '''
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1,n):
            dp[i][i+1] = i
        for low in range(n-1, 0 ,-1):
            for high in range(low+1, n+1):
                #核心算法--> 从最大的中选最小的
                # 1 要么是猜测左侧 要么是猜测右侧
                # 2从这里面选最大的 加上 x 也就是猜测拿下的钱
                # 3 从中选最小的 放入dp数组之中
                dp[low][high] = min(x + max(dp[low][x-1], dp[x+1][high]) for x in range(low,high))
        return dp[1][n]