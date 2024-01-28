class Solution:
    '''经典dp 青蛙过河
    '''
    def canCross(self, stones: List[int]) -> bool:
        size = len(stones)
        ## state 定义状态 dp[i][k] 表示为：青蛙能否以长度为 k 的距离，到达第 i 块石子。
        dp = [[False for _ in range(size + 1)]for _ in range(size)]
        dp[0][0] = True # 状态初始化
        for i in range(1,size):
            for j in range(i):
                # k 表示目标石头 和 当前石头 j 的距离
                k = stones[i] - stones[j]
                if k <= 0 or k > j + 1 : # can not reach or already reach. max k = j + 1, 青蛙跳的距离最多是跳的次数+1
                    continue
                dp[i][k] = dp[j][k] or dp[j][k-1] or dp[j][k+1] ##状态转移方程

                ## can reach i's stone
                if dp[size - 1][k]:
                    return True

        return False