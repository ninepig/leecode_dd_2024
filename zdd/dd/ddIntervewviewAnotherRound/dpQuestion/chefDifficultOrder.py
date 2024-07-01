'''
I own a restaurant and hire various chefs for specific expertise and need to find the maximum profit from the orders.
i.e.
input :
chef expertise :  [1,1,2,2,1,3,4,4] : ith chef can make specific num dish
chef profit level: [4,5,1,3,9,2,3,4] : ith chef can make specific profit by cooking that dish
Dish orders: [1,4,1,4,2,3] : I have list of orders and need to maximize the profit.

for the above example, I have 8 chefs, who can make specific dishes and make a specific profit.
for example,
0th chef can make dish 1 with a profit $4
1st chef can make dish 1 with a profit $5
....

I can assign any number of dishes to any chef and want to maximize the profit, how can I assign and what will be the final maximum profit:
for the above example,
Dish Orders :   [1,4,1,4,2,3] : Profit I can make with  best chef expertise for specific dish : [9, 4, 9, 4, 3, 2] = 27

这道题就是个简单的hashmap iteration。。感觉有问题。

这道题不是826 ===》 定义不同的， 而且原题很简单 就是一个hashmap 可以解决的问题

https://leetcode.com/discuss/interview-question/1657195/doordash-senior-software-engineer-e5-onsite-interview-dec-2021

826 是 worker 从 order里选 profit 是order带的
这道题是 dish 让厨师选。 profit 是厨师带的
而且这道题是厨师指定某个dish 能做， 而不是小于多少的能做。
所以要仔细读题

'''
class orignalSolution:
    def maxProfitAssignment(self,chef_dish:list[int],chef_profit:list[int],order:list[int]):
        ## check corner case
        dish_profit = dict()
        for i in range(len(chef_dish)):
            if chef_dish[i] not in dish_profit:
                dish_profit[chef_dish[i]] = chef_profit[i]
            else:
                ## update most profit for target dish
                if dish_profit[chef_dish[i]] < chef_profit[i]:
                    dish_profit[chef_dish[i]] = chef_profit[i]
        res = 0
        for item in order:
            if item in dish_profit:
                res += dish_profit[item]

        return res

# chef_dish = [1,1,2,2,1,3,4,4]
# chef_profit = [4,5,1,3,9,2,3,4]
# dish_order = [1,4,1,4,2,3]
# sol = orignalSolution()
# print(sol.maxProfitAssignment(chef_dish,chef_profit,dish_order))


'''这个是826套皮原题， 如果是dish_difficlut + dish_profit + chef_ability 就这么做
    我感觉最近改过题了。贴近826
有一群厨师，每个厨师有一些技能scale。有一堆菜谱，每个菜谱有一个难度scale，
和做这个菜的收益。每个厨师只能做自己能力范围内的菜，每个厨师只能做一道菜，多个厨师可以做同一道菜。求这些厨师能达到的最大收益。
https://www.1point3acres.com/bbs/thread-909410-1-1.html

https://www.1point3acres.com/bbs/thread-1030222-1-1.html
这个似乎是不一样的问法


这个题只要搞懂了 面试就算有变化也不担心
'''

'''
时间复杂度：O(NlogN+QlogQ)，其中 NNN 是任务个数，QQQ 是工人数量。
空间复杂度：O(N)，jobs 的额外空间。
链接：https://leetcode.cn/problems/most-profit-assigning-work/solutions/22424/an-pai-gong-zuo-yi-da-dao-zui-da-shou-yi-by-leetco/
'''
class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        order_profit = sorted(zip(difficulty, profit), key=lambda x: x[0])
        # order_profit.sort()
        ans = 0
        idx = 0
        best = 0
        # 为了节省循环， 当2号工人做不了3号单，他只能取他最多的值， 所以best要写在外面。
        # best 是到目前为止当前工人能做的单子 最高的收益
        ## 正相关才可以这么做
        for skill in sorted(worker):
            while idx < len(order_profit) and skill >= order_profit[idx][0]:  ## if worker can do this order, we found difficult order current worker can do
                best = max(best, order_profit[idx][1])  ## get largest profit
                idx += 1
            ans += best
        return ans

    ## o(n2)
    def maxProfitAssignmentSqureN(self,difficult:list[int],profit:list[int],worker:list[int]):
        order_profit = sorted(zip(difficult,profit),key=lambda x:x[0])
        ans = 0
        for skill in sorted(worker):
            best = 0
            idx = 0 ## loop from 0 for each time in case profit is not 正相关
            while idx < len(order_profit) and skill >= order_profit[idx][0]: ## if worker can do this order, we found difficult order current worker can do
                best = max(best,order_profit[idx][1]) ## get largest profit
                idx += 1
            ans += best
        return ans

difficulty =[2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
sol = Solution()
print(sol.maxProfitAssignment(difficulty,profit,worker))

## 如果是原题， 也就是厨师的价格

