class Solution:
    '''
    完全背包问题：
    需要确认是否可以重复使用同一个item
    还有这个题dd的tricky 是double的类型， 精度是2位
    '''
    def getMaxCalories(self,prices:list,calories:list,budget):
        # sanity check
        if not prices or not calories or not budget:
            return 0

        size = len(prices)
        prices_int = [item * 100 for item in prices]
        budget *= 100
        ## dp[i][j] means till ith item, jth budget, max calory we can get
        dp = [[0 for _ in range(budget + 1)] for _ in range(size + 1)]
        for i in range(1,size + 1):
            for b in range(1,budget + 1):
                ## if we can use not this item, mean , price is bigger than bugest
                if b < prices_int[i - 1] :
                    dp[i][b] = dp[i-1][b]
                else:
                    ## one item mult time 完全背包
                    ## max calory value is if we want pick this item .. since this is mult item
                    dp[i][b] = max(dp[i-1][b],dp[i][b-prices_int[i-1]] + calories[i-1])
                    ## one item one time  01背包
                    # dp[i][b] = max(dp[i-1][b],dp[i-1][b-prices_int[i-1]] + calories[i-1])

        return dp[-1][-1]


calories = [100,200,50]
prices = [4,10, 20]
budget = 31

sol = Solution()
print(sol.getMaxCalories(prices, calories, budget))
