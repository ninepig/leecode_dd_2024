from typing import List
'''
https://www.1point3acres.com/bbs/thread-1023872-1-1.html
https://www.1point3acres.com/bbs/thread-947601-1-1.html
https://leetcode.com/discuss/interview-question/4703815/Doordash-Phone-Interview%3A-Maximum-calories
完全背包问题

题目是给两个list，一个是食物的calorie，一个是price，然后再给一个budget，要求计算出来在这个budget之下，能获得的最多的calorie，每种食物可以多选。
标准方法是应该用dp来解决，如果用backtrack，基本上就是 Math.max(cMax, getMaxCalorie(calorieList, priceList, budget-price[i]) + colorie[i])
题目还有一个trick，是price都是double类型，得先转成int型，要不然浮点数计算有个testcase过不去。
'''

def maxCalories(prices: List[int], calories: List[int], budget: int) -> int:
    memo = {}

    def maxCal(index: int, remBudget: int) -> int:
        nonlocal memo

        if index == len(calories):
            return 0
        if remBudget in memo:
            return memo[remBudget]
        skip = maxCal(index + 1, remBudget)
        if remBudget - prices[index] < 0:
            return skip
        take = calories[index] + maxCal(index + 1, remBudget - prices[index])

        memo[remBudget] = max(skip, take)
        return memo[remBudget]

    return maxCal(0, budget)

## time o(n*w) space o(n*w)
def maxCaloriesOneItem(prices: list[int], calories: list[int], budget: int) -> int:
    size = len(prices)
    dp = [[0 for _ in range(budget + 1)] for _ in range(size + 1)]

    for i in range(1, size + 1):
        for w in range(budget + 1):
            ## can not afford i - 1's item
            if w < prices[i - 1]:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - prices[i - 1]] + calories[i - 1])

    return dp[size][budget]


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



## time o(n*w) space o(n*w)
def maxCaloriesMulItem(prices: list[int], calories: list[int], budget: int) -> int:
    size = len(prices)
    dp = [[0 for _ in range(budget + 1)] for _ in range(size + 1)]

    for i in range(1, size + 1):
        for w in range(budget + 1):
            ## can not afford i - 1's item
            if w < prices[i - 1]:
                dp[i][w] = dp[i - 1][w]
            else:
                # dp[i][w] 取「前 i - 1 种物品装入budget为 w 的背包中的最大价值」
                # 与「前 i 种物品装入budget为 w - price[i - 1] 的背包中，
                # 再装入 1 件第 i - 1 种物品所得的最大价值」两者中的最大值
                dp[i][w] = max(dp[i - 1][w], dp[i][w - prices[i - 1]] + calories[i - 1])

    return dp[size][budget]

    def completePackMethod3(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]

        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 正序枚举背包装载重量
            for w in range(weight[i - 1], W + 1):
                # dp[w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」与「前 i 种物品装入载重为 w - weight[i - 1] 的背包中，再装入 1 件第 i - 1 种物品所得的最大价值」两者中的最大值
                dp[w] = max(dp[w], dp[w - weight[i - 1]] + value[i - 1])

        return dp[W]
    
calories = [200, 50]
prices = [10, 20]
budget = 31

print(maxCaloriesOneItem(prices, calories, budget))
## 神奇啊 对了。。
print(maxCaloriesMulItem(prices, calories, budget))