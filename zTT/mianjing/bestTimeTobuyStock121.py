'''
121 + 721 套餐
https://www.1point3acres.com/bbs/thread-1066777-1-1.html
'''
from typing import List

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        只能买一次， 所以我们需要在iterating的时候 不断寻找最低点，以及计算最多的利润
        贪心法
        :param prices:
        :return:
        '''
        if not prices or len(prices) == 0:
            return 0
        lowest_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] > lowest_price:
                max_profit = max(max_profit, prices[i] - lowest_price)
            else:
                lowest_price = prices[i]
        return max_profit


# transcation fee

class Solution:
  def maxProfit(self, prices: List[int], fee: int) -> int:
    sell = 0
    hold = -math.inf

    for price in prices:
      sell = max(sell, hold + price)
      hold = max(hold, sell - price - fee)

    return sell