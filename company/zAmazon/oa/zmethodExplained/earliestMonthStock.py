# https://www.1point3acres.com/bbs/thread-1063763-1-1.html

"""

The interns at Amazon were asked to review the company's stock value over a period. Given the stock prices of n months, the net price change for the ith month is defined as the absolute difference between the average of stock prices for the first i months and for the remaining (n - i) months where 1 ≤ i < n. Note that these averages are rounded down to an integer.

Given an array of stock prices, find the month at which the net price change is minimum. If there are several such months, return the earliest month.

Note: The average of a set of integers here is defined as the sum of integers divided by the number of integers, rounded down to the nearest integer. For example, the average of [1, 2, 3, 4] is the floor of (1 + 2 + 3 + 4) / 4 = 2.5 and the floor of 2.5 is 2.

Explanation to myself

preFS:   [1   4   6  10  15]
postFS:  [15  14  11  9  5]

iterate from 0 till -2 index

         [1, 3, 2, 4, 5]
          |
          1-14/4=1-3
             |
             4/2 - 11/3= 2-3
                 |
                 6/3-9/2=2-4
                    |
                    10/4-5/1 = 2-5

"""


def getEarlyMonth(stock):
    prefixSum, postFixSum = [],[]
    N = len(stockPrice)
    summ = 0
    for p in stockPrice:
        summ += p
        prefixSum.append(summ)
    summ = 0
    for p in reversed(stockPrice):
        summ += p
        postFixSum.append(summ)
    postFixSum.reverse()


    net_change = []
    ## Main iteration
    for i in range(N-1): # we do not need the last index
        preAverage = prefixSum[i] // (i+1)
        postAverage = postFixSum[i+1] // (N-i-1)
        net_change.append(abs(preAverage-postAverage))

    min_value = min(net_change)

    res = 0

    for i in range(len(net_change)):
        if net_change[i] == min_value:
            print("RESULT: ", i+1)
            res = i + 1

    return res

stockPrice = [1, 3, 2, 3]
# stockPrice = [1, 3, 2, 4, 5]
print(getEarlyMonth(stockPrice))