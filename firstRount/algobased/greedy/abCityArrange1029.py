'''
我们先假设所有人都去了城市 a。然后令一半的人再去城市 b。现在的问题就变成了，让一半的人改变城市去向，从原本的 a 城市改成 b 城市的最低费用为多少。

已知第 i 个人更换去向的费用为「去城市 b 的费用 - 去城市 a 的费用」。所以我们可以根据「去城市 b 的费用 - 去城市 a 的费用」对数组 costs 进行排序，让前 n 个改变方向去城市 b，后 n 个人去城市 a。

最后统计所有人员的费用，将其返回即可。

贪心题
其实关键是
不是找谁最便宜,而是差价的排序. 因为所有人都需要去某个地方
所以按照 去b - 去a 的价格排序.
所以前n个人去b , 后n个人去a
'''

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[1]-x[0])
        size = len(costs)//2
        cost = 0
        for i in range(size):
            # go city b first
            cost += costs[i][1]
            # go city a in sechalf
            cost += costs[i+size][0]

        return cost