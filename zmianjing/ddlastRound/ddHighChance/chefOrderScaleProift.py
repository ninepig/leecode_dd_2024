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

class solution:
    def getMaxPorift(self,chefs:list[int],orderScale:list[int],orderProfit:list[int])->int:
        if not chefs or not orderScale or not orderProfit :
            return 0
        if len(chefs)==0 or len(orderScale)== 0 or len(orderProfit) == 0 or len(orderProfit) != len(orderScale):
            return 0
        scale_profit = sorted(zip(orderScale,orderProfit),key=lambda x:x[0]) ## get orderScale, Profit tuple, sorted with scale aseding
        idx = 0
        res = 0
        best = 0 ## profit  chef can get most under his scale
        for chef in sorted(chefs):
            ## 这里必须是 》= 因为difficult 可能duplicated，
            while idx < len(scale_profit) and chef >= scale_profit[idx][0]: ## find most profit under his scale
                best = max(best,scale_profit[idx][1]) ##profit如果和难度不线性,所以只要这里best 是取max的情况下 就能满足
                ## 因为 best根据能做的保证最大， chef是sort以后的。所以这样肯定满足
                idx += 1
            res += best

        return res

    ## 不需要2 1 就够用了
    def getMaxPorif2(self,chefs:list[int],orderScale:list[int],orderProfit:list[int])->int:
        if not chefs or not orderScale or not orderProfit :
            return 0
        if len(chefs)==0 or len(orderScale)== 0 or len(orderProfit) == 0 or len(orderProfit) != len(orderScale):
            return 0
        scale_profit = sorted(zip(orderScale,orderProfit),key=lambda x:x[0]) ## get orderScale, Profit tuple, sorted with scale aseding
        res = 0
        for chef in sorted(chefs):
            idx = 0
            best = 0
            ## 这里必须是 》= 因为difficult 可能duplicated，同等情况下 可能profit会高 ,如果profit 不和难度正比的话 我们就要这么做
            while idx < len(scale_profit) and chef >= scale_profit[idx][0]: ## find most profit under his scale
                best = max(best,scale_profit[idx][1])
                idx += 1
            res += best

        return res

    ## followUp 详见 https://www.1point3acres.com/bbs/thread-904367-1-1.html
    ##：假设skill和difficulty都是1-100的整数，
    ## 要求用O(M+N)的时间 用bucket的概念，找到每个skill 对应的最大profit
    ## 这么一看好像就是之前地里的那个面经

    ## 因为 scale 有duplicated 先利用一个bucket 算出 scale：单个profit（最大） 的mapping
    ## [0, 0, 10, 0, 40, 0, 20, 0, 40, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ## 然后再loop一边 把其他的scale可以获得的profit 都填满， 比如小于2的就是0 2--4的就是10 以此类推
    ## [0, 0, 10, 10, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
    ##然后根据 chef的水平找到这个scale 可以获取的最大收益，
    def findTotalProfitNoSorting(self,chefs:list[int],orderScale:list[int],orderProfit:list[int])->int:
        scaleMaxProfitBucket = [0 for _ in range(100 + 1)]
        orderNumber = len(orderScale)

        ## get profit for each bucket
        for i in range(orderNumber):
            scale = orderScale[i]
            profit = orderProfit[i]
            ## get (scale)-largest profit dict , if we have duplciated scale, we choose larget profit
            ## 这样就和一个leetcode的面经对上了
            scaleMaxProfitBucket[scale] = max(scaleMaxProfitBucket[scale],profit)
        #print(scaleMaxProfitBucket)
        skill_profit_all_Bucket = [0 for _ in range(100 + 1)]
        maxProfit = 0
        for i in range(len(scaleMaxProfitBucket)):
            maxProfit = max(maxProfit,scaleMaxProfitBucket[i])
            skill_profit_all_Bucket[i] = maxProfit ## 这样就可以算出对于每个skale 最大的profit
        #print(skill_profit_all_Bucket)
        totalProfit = 0
        for chef in chefs:
            totalProfit += skill_profit_all_Bucket[chef]

        return totalProfit


if __name__ == "__main__":
    chefs = [5,4,3,7] ## [40,25,25]
    difficult = [2,4,6,8,10] # [85,47,57]
    profit = [10,40,20,40,50] # [24,66,99]
    sol = solution()
    print(sol.getMaxPorift(chefs, difficult, profit))
    print(sol.findTotalProfitNoSorting(chefs,difficult,profit))


