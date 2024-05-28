'''
121 + 721 套餐
https://www.1point3acres.com/bbs/thread-1066777-1-1.html
'''
import math
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

## one
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0
        if len(prices) < 2:
            return result

        lowest = prices[0]
        for i in range(1, len(prices)):
            current = prices[i]

            # capture any gains immediately
            # by selling and then buying at the same price of prices[i]
            if current > lowest:
                result += (current - lowest)

            # otherwise, current <= lowest
            # if current == lowest: no harm updating without adding to result
            # if current < lowest: should update lowest to get max profit later on

            # simulates buying at current price (if we sell later)
            # or not buying at all (since no adding to result)
            lowest = current

        return result


# transcation fee
'''
Initialize two variables: buy and sell. Set buy to negative infinity and sell to zero.
 These variables will keep track of the maximum profit at each day.

Iterate through the prices of the stocks starting from the first day.

Update the buy variable by taking the maximum of its current value and the previous sell value minus the stock price.
This represents the maximum profit after buying the stock.
buy = max(buy, sell - price)

Update the sell variable by taking the maximum of its current value and
the previous buy value plus the stock price minus the transaction fee.
This represents the maximum profit after selling the stock.
sell = max(sell, buy + price - fee)

After iterating through all the prices, the maximum profit will be stored in the sell variable.

Return the value of sell as the maximum profit.

'''
class Solution:
    ## we can only do one transcation
    ## fee is charged on sell(buy + sell)
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = float('-inf')
        sell = 0

        for price in prices:
            ## greedy
            ## This represents the maximum profit after buying the stock.
            buy = max(buy, sell - price)
            ## max profit after we sell the stock
            sell = max(sell, buy + price - fee)

        return sell