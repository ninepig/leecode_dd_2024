## https://www.cnblogs.com/anzhengyu/p/11408466.html

class Solution:
    # 思路 1：动态规划 + 二维基本思路
    def zeroOnePackMethod1(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]

        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 第 i - 1 件物品装不下
                if w < weight[i - 1]:
                    # dp[i][w] 取「前 i - 1 件物品装入载重为 w 的背包中的最大价值」
                    dp[i][w] = dp[i - 1][w]
                else:
                    # dp[i][w] 取「前 i - 1 件物品装入载重为 w 的背包中的最大价值」与「前 i - 1 件物品装入载重为 w - weight[i - 1] 的背包中，
                    # 再装入第 i - 1 物品所得的最大价值」两者中的最大值
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight[i - 1]] + value[i - 1])

        return dp[size][W]

# dp[i][w] 前i件物品 装到最大w的背包之中可以获得最大的价值
# 初始化 0
# 状态转移 对于第 i 件物品。
# 1 他对于当前w值， 他装不下 --》 dp[i][w] = dp[i-1][w]  不装丫
# 2 他装得下 dp[i][w] = dp[i-1][w]  dp[i -1 ] [ w - weight[i - 1]] + value[i-1] # 装他 和不装他的最大价值

    def zeroOnePackMethod2(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]

        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 逆序枚举背包装载重量（避免状态值错误）
            for w in range(W, weight[i - 1] - 1, -1):
                # dp[w] 取「前 i - 1 件物品装入载重为 w 的背包中的最大价值」与「前 i - 1 件物品装入载重为 w - weight[i - 1] 的背包中，再装入第 i - 1 物品所得的最大价值」两者中的最大值
                dp[w] = max(dp[w], dp[w - weight[i - 1]] + value[i - 1])

        return dp[W]
