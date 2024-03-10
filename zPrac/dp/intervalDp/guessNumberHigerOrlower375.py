from cmath import inf


class Solution:
    '''374的进化 因为需要知道具体的金钱额度， 所以没有办法用bs来做
    必须是dp

    state[i][j] 在 i---j 区间我们要赢最小要花多少钱
    state[i][i] = 0 一次猜中就不需要花钱。 或者只有一个数的情况下， state[i][j] == inf 无穷大的钱作为初始化
    state transfer = min(state[i][k-1]  , state[k + 1][j]) + k

    https://algo.itcharge.cn/Solutions/0300-0399/guess-number-higher-or-lower-ii/#%E6%80%9D%E8%B7%AF-1-%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92
    if x == target --> we win, pay 0
    if x <= target , we pay min(1--x-1) plus x , we win
    if x >= target we pay min(x+1, n) plus x, we win

    return state[1][n]
    '''
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
        for length in range(2,n+1):# 跨度
            for l in range(1,n + 1): # 左侧位置
                r = l + length - 1 # 右侧位置
                dp[l][r] = inf
                for k in range(l,r + 1): # 对于k的钱 我们在 l--r区间计算
                    ## 在左右侧，我们确保要获得胜利，所以我们需要准备两侧较大获胜较大的值
                    # 然后我们取所有最小的值
                    dp[l][r] = min(dp[l][r],max(dp[l][k - 1] + k, dp[k + 1][r] + k))

        return dp[1][n]
