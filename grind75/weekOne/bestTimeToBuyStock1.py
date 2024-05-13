import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## 最基本的 stock题 ， 其实就是找最低的值， 同时每个数和最低值计算差值
        ## 基本的贪心法，只考虑当前情况下最低的情况，然后获得最大的利润。
        if not prices or len(prices) == 0:
            return 0
        lowest = math.inf
        max_profit = 0
        for i in range(len(prices)):
            if lowest > prices[i]:
                lowest = prices[i]
            else:
                max_profit  = max(max_profit, prices[i] - lowest)

        return max_profit
