'''
https://leetcode.cn/problems/frog-jump/solutions/750427/gong-shui-san-xie-yi-ti-duo-jie-jiang-di-74fw
青蛙过河
'''
from typing import List


class Solution:
    def canReach(self, stones:list[int]) -> bool:
        size = len(stones)
        stone_table = dict()
        for i in range(size):
            ##这个stone的value代表的是stone在河流里的位置， i 则只是第几个块石头。 所以必须满足 stone value才能reach
            ## key is the value of stone, means we need how many step to reach that. value is the stone Number, pos
            stone_table[stones[i]] = i # 石头所在的单元格信息

        if not stone_table[1]:
            return False # step one  we fixed 1 step

        def dfs(current_pos,last_step):
            if current_pos == size - 1:
                return True # we can reach end of stone
            for i in range(-1,2):
                if last_step + i == 0 : # not move
                    continue
                next = stones[current_pos] + last_step + i # stone(value) we can reach
                if next in stone_table : # can be reach
                    flag = dfs(next,last_step + i)
                    if flag:
                        return True
            return False

        return dfs(1,1) # from pos 1, step is 1


    def canReachWithMemo(self, stones:list[int]) -> bool:
        size = len(stones)
        stone_table = dict()
        for i in range(size):
            ## key is the value of stone, means we need how many step to reach that. value is the stone Number, pos
            stone_table[stones[i]] = i # 石头所在的单元格信息

        memo = dict()

        if not stone_table[1]:
            return False # step one  we fixed 1 step

        def dfs(current_pos,last_step):
            if current_pos == size - 1:
                return True # we can reach end of stone
            if memo[(current_pos, last_step)] :
                return memo[(current_pos ,last_step)]
            for i in range(-1,2):
                if last_step + i == 0 : # not move
                    continue
                next = stones[current_pos] + last_step + i # stone we can reach
                if next in stone_table : # can be reach
                    flag = dfs(next,last_step + i)
                    memo[(current_pos, last_step)] = flag
                    if flag:
                        return True
            return False

        return dfs(1,1) # from pos 1, step is 1

    def canCrossDp(self, stones: List[int]) -> bool:
        size = len(stones)

        dp = [[False for _ in range(size + 1)] for _ in range(size)]
        dp[0][0] = True

        for i in range(1, size):
            for j in range(i):
                k = stones[i] - stones[j]
                if k <= 0 or k > j + 1: # if not move or can not move j + 1
                    continue
                dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                if dp[size - 1][k]:
                    return True

        return False