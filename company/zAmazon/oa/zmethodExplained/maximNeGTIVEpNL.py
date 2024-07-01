# https://www.fastprep.io/problems/amazon-maximize-negative-pnl_months
import heapq


'''
You are analyzing the market trends of Amazon stocks. An AWS financial service model returned an array of integers, PnL (Profit and Loss), for your portfolio representing that in the ith month, you will either gain or lose PnL[i]. All reported PnL values are positive, representing gains.

As part of the analysis, you will perform the following operation on the PnL array any number of times:

Choose any month (0 ≤ i < n) and multiply PnL[i] by -1
Find the maximum number of months you can afford to face a loss, i.e., have a negative PnL, such that the cumulative PnL for each of the n months remains strictly positive i.e. remains greater than 0.
'''
##别人的答案
'''
A PriorityQueue (min-heap) is used to efficiently select the smallest PnL values for potential flipping.
 This queue stores all PnL values from the input array.
We calculate the total PnL to keep track of the overall profitability. 
This is crucial for ensuring that flipping a month's PnL doesn't result in a non-positive cumulative PnL.
We iteratively remove the smallest PnL value from the queue and check if flipping it (i.e., multiplying it by -1 and thus subtracting twice its value from the total PnL) would still keep the total PnL positive. If yes, we increment the count of maximum negative months and adjust the total PnL accordingly.
The process stops as soon as flipping the current smallest PnL value would make the total PnL non-positive or when there are no more PnL values to consider.
'''

class Solution:
    def maximizeNegativePnLMonths(self, PnL: list[int]) -> int:
        minStack = []
        prefixSum = dict()
        currSum = 0

        for i, price in enumerate(PnL):
            currSum += price
            heapq.heappush(minStack, (price, -i))
            prefixSum[i] = currSum

        finish = False
        counter = 0
        while not finish:
            neg, index = heapq.heappop(minStack)
            index *= -1
            while index < len(PnL):
                if prefixSum[index] - 2 * neg > 0:
                    prefixSum[index] -= 2 * neg
                    index += 1
                else:
                    finish = True
                    break
            if not finish:
                counter += 1

        return counter




solution = Solution()
# pnl = [5, 3, 1, 2]
# pnl = [1, 1, 1, 1, 1]
pnl = [5, 2, 3, 5, 2, 3]
print(solution.maximizeNegativePnLMonths(pnl))

