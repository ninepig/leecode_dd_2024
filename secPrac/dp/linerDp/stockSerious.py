'''
最基本的股票1
只能在某一天买入，
未来某一天卖掉
1 bf
循环两次

todo 第四题可以用优先队列来做？ 好像面试有提过 先放在这里

'''
from typing import List


class SolutionStock1:
    def maxProfitBF(self, prices: List[int]) -> int:
        res = 0
        size = len(prices)
        for i in range(size):
            for j in range(i + 1 ,size):
                if prices[j] > prices[i]:
                    res = max(res, prices[j] - prices[i])

        return res

    ''' 
    只能和后面的比， 所以我们可以每次都找新的低点 然后和后面的比
    有比它大的 更新利润
    有比它小的 更新他
    '''
    def maxProfitBF(self, prices: List[int]) -> int:
        res= 0
        size = len(prices)
        lowest = prices[0]
        for i in range(1,size):
            if prices[i] > lowest:
                res = max(res, prices[i] - lowest)
            elif prices[i]<= lowest:
                lowest = prices[i]

        return res

'''
可以买卖1只股票（同时持有）。
不断地买卖
这个题只要有利润就搞
'''
class SolutionStock2:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        size = len(prices)
        for i in range(size):
            for j in range(1,size):
                if prices[j] > prices[i]:
                    res += prices[j] - prices[i]
                    i = i+1 #这个在python里没法用 所以不能用这种loop
                    break
                    # 完成一笔i就用掉了
        return res

    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        # checking if the number current stock is greater than previous, just add the difference
        # 用这种loop 比较好
        for i in range(1,len(prices)):
            if (prices[i] > prices[i-1]): #这样就避免了2重循环 无法给i+1的尴尬
                res += prices[i] - prices[i-1]
        return res

'''
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/solutions/2199035/yi-tao-mo-ban-ji-xing-dai-ma-bi-zhao-yan-0ap8
神奇模板'''


'''
dp[0,0,0,0] 一个思维tuble代表阶段
0th in tuble, own money in first buy
1th in tuble, earned money after first sell
2th in tuble, money after second buy,
3th in tuble, money after second sell
'''
class SolutionStock3:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        dp = [[0, 0, 0, 0] for _ in range(size)]
        dp[0] = [-prices[0],0,-prices[0],0] # 第一天可以做的操作
        for i in range(1,size):
            dp[i][0] = max(dp[i-1][0],-prices[i]) # 要么不买，要么是欠第一个票的钱
            dp[i][1] = max(dp[i-1][1],prices[i] + dp[i-1][0]) # 因为dp[i-1][0]是负的 所以用加号，把第二天的价格减去第一天的价格
            dp[i][2]= max(dp[i-1][2],dp[i-1][1] - prices[i])  # 第二天买之前， 要么不买 要么就是之前的利润减去当前股票的价格
            dp[i][3] = max(dp[i-1][3],prices[i] + dp[i-1][2]) # 第二天卖， 要么获得当前股票价格，当然要减去买时候的成本，要么就不做动作

        return dp[-1][-1]


# 把3 推进下就行
class SolutionStock4:
    def maxProfit(self, k:int, prices: List[int]) -> int:
        size = len(prices)
        dp = [[0,0]*k for _ in range(size)]
        dp[0] = [-prices[0],0] * k ## k对应的k 笔交易  参考stock3
        for i in range(1,size):
            for j in range(k):
                # 买入, 要么不操作， 要么就是 付钱 要把之前的利润拿出来
                dp[i][j*2] = max(dp[i-1][j*2],-prices[i] + (dp[i-1][j*2-1] if j != 0 else 0))
                # 卖出: 要么不操作， 要么就是收钱， 把当前的票价值加入
                dp[i[j*2 + 1]] = max(dp[i-1][j*2 + 1], prices[i] + dp[i-1][j*2])

        return dp[-1][-1]


## 卖出以后要冷冻一天 ，所以你买入必须是上次卖出后的2天
class SolutionStockWithFree:
    def maxProfit(self, k:int, prices: List[int]) -> int:
        size = len(prices)
        dp = [[0,0] for _ in range(size)]
        for i in range(1,size):
            # 对于第i天的买入， 要么不操作， 要么是两天前卖出的最大值 - 当前price
            dp[i][0] = max(dp[i-1][0], -prices[i] + (dp[i-2][1] if i<2 else 0 ))
           #对于第i天的卖出，要么不操作，要么拿到当前的股票价值
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])

        return dp[-1][-1]


#完全跟着模板来，特别轻松。。。
class SolutionWithFee:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)
        dp = [[0,0] for _ in range(size)]
        for i in range(1,size):
            dp[i][0] = max(dp[i-1][0],-prices[i]+dp[i-1][1])
            dp[i][1] = max(dp[i-1][0],prices[i] + dp[i-1][0] - fee)

        return dp[-1][-1]