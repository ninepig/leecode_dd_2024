# https://www.1point3acres.com/bbs/thread-1023872-1-1.html
# https://www.1point3acres.com/bbs/thread-947601-1-1.html
# https://leetcode.com/discuss/interview-question/4703815/Doordash-Phone-Interview%3A-Maximum-calories
# 完全背包问题
#
# 题目是给两个list，一个是食物的calorie，一个是price，然后再给一个budget，要求计算出来在这个budget之下，能获得的最多的calorie，每种食物可以多选。
# 标准方法是应该用dp来解决，如果用backtrack，基本上就是 Math.max(cMax, getMaxCalorie(calorieList, priceList, budget-price[i]) + colorie[i])
# 题目还有一个trick，是price都是double类型，得先转成int型，要不然浮点数计算有个testcase过不去。


class Solution:
    def getMaxCalories(self,prices:list[int],calories:list[int],budget:int):
        if not prices or not calories or budget <= 0:
            raise Exception("input wrong")

        if len(prices) != len(calories):
            raise Exception("input wrong")
        '''
        dp[i][b] i means i th item, w means budget --> max calorize we can get
        iniial
        dp[x][y] = 0 
        dp transfer
        max( not pick i th item, pick one more ith item since we can put mult same items )
        dp[i][b] = max(dp[i-1][b], dp[i][b - price[i] + calorie[i])
        '''
        N = len(prices)
        dp = [[0 for _ in range(budget + 1)] for _ in range(N + 1)]
        for i in range(1,N+1):
            for b in range(budget + 1):
                if b < prices[i - 1]: # if we dont have budget for current item
                    dp[i][b] = dp[i-1][b] ## we can not pick ith item
                else:
                    ## only take one item
                    # one_item =  max(dp[i-1][b], dp[i - 1][b-prices[i-1]] + calories[i-1])
                    ## mult item
                    # two_item = max(dp[i-1][b], dp[i][b-prices[i-1]] + calories[i-1])
                    dp[i][b] = max(dp[i-1][b], dp[i][b-prices[i-1]] + calories[i-1])

        return dp[-1][-1]

    def getMaxCaloriesDouble(self,prices:list[int],calories:list[int],budget:float):
        if not prices or not calories or budget <= 0:
            raise Exception("input wrong")

        if len(prices) != len(calories):
            raise Exception("input wrong")

        budget = budget * 100
        prices = [item * 100 for item in prices]
        '''
        dp[i][b] i means i th item, w means budget --> max calorize we can get
        iniial
        dp[x][y] = 0 
        dp transfer
        max( not pick i th item, pick one more ith item since we can put mult same items )
        dp[i][b] = max(dp[i-1][b], dp[i][b - price[i] + calorie[i])
        '''
        N = len(prices)
        dp = [[0 for _ in range(budget + 1)] for _ in range(N + 1)]
        for i in range(1,N+1):
            for b in range(budget + 1):
                if b < prices[i - 1]: # if we dont have budget for current item
                    dp[i][b] = dp[i-1][b] ## we can not pick ith item
                else:
                    ## only take one item
                    # one_item =  max(dp[i-1][b], dp[i - 1][b-prices[i-1]] + calories[i-1])
                    ## mult item
                    # two_item = max(dp[i-1][b], dp[i][b-prices[i-1]] + calories[i-1])
                    dp[i][b] = max(dp[i-1][b], dp[i][b-prices[i-1]] + calories[i-1])

        return dp[-1][-1]

    ## 不考虑
    def completePackMethod3(self, prices:list[int], calories:list[int], budget: int):
        size = len(prices)
        budget = budget * 100
        prices = [item * 100 for item in prices]
        dp = [0 for _ in range(budget + 1)]
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 正序枚举背包装载重量
            for w in range(prices[i - 1], budget + 1):
                # dp[w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」与「前 i 种物品装入载重为 w - weight[i - 1] 的背包中，再装入 1 件第 i - 1 种物品所得的最大价值」两者中的最大值
                dp[w] = max(dp[w], dp[w - prices[i - 1]] + calories[i - 1])

        return dp[budget]

calories = [100,200,50]
prices = [4,10, 20]
budget = 31

sol = Solution()
print(sol.getMaxCalories(prices, calories, budget))
print(sol.getMaxCaloriesDouble(prices, calories, budget))
print(sol.completePackMethod3(prices, calories, budget))