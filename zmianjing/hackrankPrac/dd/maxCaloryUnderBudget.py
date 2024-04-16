# 题目是给两个list，一个是食物的calorie，一个是price，然后再给一个budget，要求计算出来在这个budget之下，能获得的最多的calorie，每种食物可以多选。
# 标准方法是应该用dp来解决，如果用backtrack，基本上就是 Math.max(cMax, getMaxCalorie(calorieList, priceList, budget-price[i]) + colorie[i])
# 题目还有一个trick，是price都是double类型，得先转成int型，要不然浮点数计算有个testcase过不去。

class Solution:
    def getMaxCaloryUnderBudget(self, calories, price, budget):
        ## santity check
        if not calories or not print or budget <= 0:
            raise Exception("wrong input")
        '''
        since we can put multtimes for single item
        complete back pack problem
        dp[i][b] , ith item under b bucket , max calory
        dp[0][0] = 0 
        dp transfer
        dp[i][b] 
        if we can afford ith item vs we can not afford
        dp[i][b] = max(dp[i - 1][b], dp[i][b - price[i]] + calorie[i - 1])
        '''

        budget = budget * 100
        price = [item * 100 for item in price]

        length = len(calories)
        dp = [[0 for _ in range(budget + 1)] for _ in range(length + 1)]

        for i in range(1, length + 1):
            for b in range(1, budget + 1):
                if b < price[i - 1]:  ## this mean we can not afford this item, dp from 1 so we need i-1 to get item
                    dp[i][b] = dp[i - 1][b]
                else:
                    dp[i][b] = max(dp[i - 1][b], dp[i][b - price[i - 1]] + calories[i - 1])

        return dp[-1][-1]


calories = [100, 200, 50]
prices = [4, 30, 20]
budget = 31
sol = Solution()
print(sol.getMaxCaloryUnderBudget(calories, prices, budget))
