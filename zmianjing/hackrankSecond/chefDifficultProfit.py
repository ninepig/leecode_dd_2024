class Solution:
    def getMaxProfit(self, chef, difficult, profit):
        if not chef or not difficult or not profit:
            print("invalid input")  ## we need add bunch of condition here
            return 0

        diff_profit = sorted(zip(difficult, profit), key=lambda x: x[0])
        idx = 0
        res = 0
        best = 0

        for item in sorted(chef):
            while idx < len(diff_profit) and item >= diff_profit[idx][0]:  # find most difficult dish current chef make
                best = max(best, diff_profit[idx][1])  ## updated best value , since we sorted by chef ability
                ## so he can choose max profit dish he can do .
                idx += 1
            res += best

        return res

    def getMaxProfitBucketSort(self, chef, difficult, profit):
        if not chef or not difficult or not profit:
            print("invalid input")  ## we need add bunch of condition here
            return 0

        diff_profit = [0 for _ in range(101)]

        ## we found largest profit for each diff can make
        for i in range(len(difficult)):
            ## updating each difficult 's value
            diff_profit[difficult[i]] = max(diff_profit[difficult[i]], profit[i])

        ## updating each skill's max profit
        skill_profit = [0 for _ in range(101)]
        best = 0
        for i in range(len(diff_profit)):
            ## 这里别写错了。
            best = max(best, diff_profit[i])  ## get max profit so far
            skill_profit[
                i] = best  ## if we did not see a profit with index, best = 0, which means , this skill is not enough to do a dish

        res = 0
        for item in chef:
            res += skill_profit[item]

        return res


chefs = [5, 4, 3, 7]  ## [40,25,25]
difficult = [2, 4, 6, 8, 10]  # [85,47,57]
profit = [10, 40, 20, 40, 50]  # [24,66,99]
# chefs = [1, 2, 3, 4]  ## [40,25,25]
# difficult = [2, 4, 6, 8, 10]  # [85,47,57]
# profit = [10, 40, 20, 40, 50]  # [24,66,99]
sol = Solution()
print(sol.getMaxProfit(chefs, difficult, profit))
print(sol.getMaxProfitBucketSort(chefs, difficult, profit))