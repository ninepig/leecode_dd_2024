## 类似leetcode 826
'''

有一群厨师，每个厨师有一些技能scale。有一堆菜谱，
每个菜谱有一个难度scale，和做这个菜的收益。每个厨师只能做自己能力范围内的菜，每个厨师只能做一道菜，
多个厨师可以做同一道菜。求这些厨师能达到的最大收益。

https://www.1point3acres.com/bbs/thread-909410-1-1.html
# - 先解释思路，问如何找到某个diffculty的最大profit
# - diffculty有dups
https://www.1point3acres.com/bbs/thread-1030222-1-1.html
第二个没懂

https://www.1point3acres.com/bbs/thread-904367-1-1.html
看这里
'''
import collections

'''
zip order Scale and order Profit
sort chef
check max value chef can reach

'''



## nlogn
def getMaxPorift(self, chefs: list[int], orderScale: list[int], orderProfit: list[int]) -> int:
    if not chefs or not orderScale or not orderProfit:
        return 0
    scale_profit = sorted(zip(orderScale,orderProfit),key=lambda x:x[0])
    sorted_chef = sorted(chefs)
    idx = 0
    max_value = 0
    res = 0
    for chef in sorted_chef:
        ## current chef 's ability bigger than scale's difficult
        while idx < len(scale_profit) and chef >= scale_profit[idx][0]:
            max_value = max(max_value,scale_profit[idx][1]) ## update value
            idx += 1 ## move idx
        res += max_value ## update every iteration

    return res

def getMaxPoriftMN(self, chefs: list[int], orderScale: list[int], orderProfit: list[int]) -> int:
    if not chefs or not orderScale or not orderProfit:
        return 0
    '''
    if we don't sort 
     bucket idea
    for each order scale profit 
    get a dict
    4,7,9,10 --> 4,6,5,8
    order scale ---> order best value
    [0,0,0,4,0,0,6,0,6,8]
    diffscale ---> order best value
    [0,0,0,4,4,4,6,6,8]
    chef ---> order value 
    get sum
    '''
    scale_maxprofit_bucket = [0 for _ in range(100 + 1)]
    order_number = len(orderScale)

    ## get profit for each bucket
    for i in range(order_number):
        scale = orderScale[i]
        profit = orderProfit[i]
        ## get (scale)-largest profit dict , if we have duplciated scale, we choose larget profit
        ## 这样就和一个leetcode的面经对上了
        scale_maxprofit_bucket[scale] = max(scale_maxprofit_bucket[scale], profit)
    # print(scaleMaxProfitBucket)
    skill_profit_all_Bucket = [0 for _ in range(100 + 1)]
    max_profit = 0
    for i in range(len(scale_maxprofit_bucket)):
        max_profit = max(max_profit, scale_maxprofit_bucket[i])
        skill_profit_all_Bucket[i] = max_profit  ## 这样就可以算出对于每个skale 最大的profit

    total_profit = 0
    for chef in chefs:
        total_profit += skill_profit_all_Bucket[chef]

    return total_profit