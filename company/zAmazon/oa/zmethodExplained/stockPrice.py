# https://www.1point3acres.com/bbs/thread-1036228-1-1.html
# https://www.1point3acres.com/bbs/thread-1037532-1-1.html
# https://www.fastprep.io/problems/count-maximum-profitable-groups

'''
A team of analysts at Amazon needs to analyze the stock prices of Amazon over a period of several months.

A group of consecutively chosen months is said to be maximum profitable if the price in its first or last month is the maximum for the group. More formally, a group of consecutive months [l, r] (1 ≤ l ≤ r ≤ n) is said to be maximum profitable if either:

stockPrice[l] = max(stockPrice[l], stockPrice[l + 1], ..., stockPrice[r])
or, stockPrice[r] = max(stockPrice[l], stockPrice[l + 1], ..., stockPrice[r])
Given prices over n consecutive months, find the number of maximum profitable groups which can be formed. Note that the months chosen must be consecutive, i.e., you must choose a subarray of the given array.
'''


## burtal force way .. 很直观。。。拉subarray 看是否成立。。
def countMaximumProfitableGroups(stockPrice):

    maximal_count = 0

    for start in range(0, len(stockPrice)):
        for end in range(start+1, len(stockPrice)+1):
            target = stockPrice[start:end]
            # print(target)

            max_in_target = max(target)

            if target[0] == max_in_target or target[-1]== max_in_target:
                maximal_count += 1

    return maximal_count


test = [2, 3, 2]
print(countMaximumProfitableGroups(test))