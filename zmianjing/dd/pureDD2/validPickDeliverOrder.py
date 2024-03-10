'''
A driver's route can be represented as follows:
Given a set list of pickups and deliveries for order, figure out if the given list is valid or not.

A delivery cannot happen for an order before pickup.
The same order cannot be delivered or picked up twice
The car must be empty at the end of the drive.
Examples below:
[P1, P2, D1, D2]==>valid


Follow up:
1 Find the longest valid subarray. O(n^2) is obvious. O(n) involves careful consideration of all the cases of invalidity.
n^2 比较简单 ，暴力法就行
2. 给定N, 打印所有valid序列
---》这个真不会。。 应该是dfs + back track？ 但这样就必须是 按顺序来的path
3. 推导计 valid序列数量的公式  https://leetcode.cn/problems/count-all-valid-pickup-and-delivery-options/solutions/1160759/shu-xue-qiu-jie-tui-dao-guo-cheng-by-che-ubmp
这道题是leetcode 1359
出的题可能不一样。
1359就是个组合脑筋题
'''

class solution:
    def judgeIfOrderIsValid(self,orders:list[str])->bool:
        if not orders or len(orders) ==0 :
            return True
        pick_set = set()
        deliver_set = set()
        for order in orders:
            if order.startswith("D"): # this is delver oder
                if order in deliver_set:
                    print("error repeated deliver order")
                    print(order)
                    return False
                deliver_set.add(order)
                ## change d to p
                pOrder = order.replace("D","P")
                if pOrder not in pick_set:
                    print("error not matching")
                    print(pOrder)
                    return False
            if order.startswith("P"):
                if order in pick_set:
                    print("error repeating pickup order")
                    print(order)
                    return False
                pick_set.add(order)

        return len(pick_set) == len(deliver_set)

tool = solution()
# test = ["P1", "D2", "D1", "P2"]
test = ["P1", "D1","P1","D1"]
'''
[P1, D1, P2, D2]==>valid
[P1, D2, D1, P2]==>invalid
[P1, D2]==>invalid
[P1, P2]==>invalid
[P1, D1, D1]==>invalid
[]==>valid
[P1, P1, D1]==>invalid
[P1, P1, D1, D1]==>invalid
[P1, D1, P1]==>invalid
[P1, D1, P1, D1]==>invalid
'''
print(tool.judgeIfOrderIsValid(test))

