
'''


如果加油站提供的油总和大于等于消耗的汽油量，则必定可以绕环路行驶一周
假设先不考虑油量为负的情况，我们从「第 0 个加油站」出发，环行一周。记录下汽油量 gas[i] 和 cost[i] 差值总和 sum_diff，同时记录下油箱剩余油量的最小值 min_sum。
如果差值总和 sum_diff < 0，则无论如何都不能环行一周。油不够啊，亲！！
如果 min_sum ≥ 0，则行驶过程中油箱始终有油，则可以从 0 个加油站出发环行一周。
如果 min_sum < 0，则说明行驶过程中油箱油不够了，那么考虑更换开始的起点。
从右至左遍历，计算汽油量 gas[i] 和 cost[i] 差值，看哪个加油站能将 min_sum 填平。如果最终达到 min_sum ≥ 0，则说明从该点开始出发，油箱中的油始终不为空，则返回该点下标。
如果找不到最返回 -1

如果存在解，则 保证 它是 唯一 的。
wenjing 这个是关键 .答案里没有说明这一点 所以需要一定的思考

'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # sum diff 表示总的油耗差 , min_sum记录下油箱剩余油量的最小值 min_sum
        sum_diff = 0
        min_sum = float('-inf')
        for i in range(len(gas)):
            sum_diff += gas[i] - cost[i]
            min_sum = min(sum_diff,min_sum)

        if sum_diff < 0:
            return -1 # no matter start from where, it can not

        if min_sum > 0:
            return 0 # unique answer, if start from 0, and min_sum bigger than 0, means it can arrive

        for i in range(1,len(gas)):
            if min_sum + gas[i] - cost[i] > 0:
                return i

        return -1