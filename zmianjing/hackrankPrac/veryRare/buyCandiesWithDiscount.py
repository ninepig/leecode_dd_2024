class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        if not cost :
            return 0
        if len(cost) <=2 :
            return  sum(cost)
        cost.sort(reverse=True)
        ## we count every 2 and skip third
        res = 0
        for idx in range(0,len(cost),3):
            res += cost[idx]
            if idx + 1 < len(cost):
                res += cost[idx + 1]
        return res

