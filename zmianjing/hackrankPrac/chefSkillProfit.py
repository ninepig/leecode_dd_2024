class Solution:
    def maxProfit(self, dish, profit, chef):
        ## santity check
        if not dish or not profit or not chef:
            raise Exception("wrong input")
            ##... length .. .size... skip for saving time

        '''
        profit not liner like dish's difficlut
        '''

        ## sort by dish' difficult
        ## nlogn for sorting
        dish_profit_sorted = sorted(zip(dish, profit), key=lambda x: x[0])
        idx = 0
        best = 0
        res = 0
        ## we sorted chef's ability, find the best profit he can make by compare to order difficult
        for item in sorted(chef):
            while idx < len(dish_profit_sorted) and item >= dish_profit_sorted[idx][0]:
                best = max(best, dish_profit_sorted[idx][1])  ## update best value
                idx += 1
            res += best

        return res

    def maxProftBucket(self, dish, profit, chef):
        ## if the input is very small , dish/profit can fit in (1---100)
        ## we can use bucket sort to do this to make to o(m+n)
        ## santity check
        ## santity check
        if not dish or not profit or not chef:
            raise Exception("wrong input")
            ##... length .. .size... skip for saving time

        dish_profit_dict = [0 for _ in range(101)]

        for i in range(len(dish)):
            ## we store largest value of dishdifficult - profit in to array
            dish_difficult = dish[i]
            cur_profit = profit[i]
            dish_profit_dict[dish_difficult] = max(cur_profit, dish_profit_dict[dish_difficult])

        skill_profit = [0 for _ in range(101)]

        best = 0
        ## update a chef skill to profit dict , we use best profit by that chef skill from dish_profit to do this
        for i in range(len(dish_profit_dict)):
            best = max(best, dish_profit_dict[i])
            skill_profit[i] = best
        res = 0
        for item in chef:
            res += skill_profit[item]

        return res


chefs = [5, 4, 3, 7]  ## [40,25,25]
difficult = [2, 4, 6, 8, 10]  # [85,47,57]
profit = [10, 40, 20, 40, 50]  # [24,66,99]
sol = Solution()
print(sol.maxProfit(difficult, profit, chefs))
print(sol.maxProftBucket(difficult, profit, chefs))
