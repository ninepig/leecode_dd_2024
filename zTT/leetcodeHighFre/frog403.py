'''
https://leetcode.cn/problems/frog-jump/solutions/750427/gong-shui-san-xie-yi-ti-duo-jie-jiang-di-74fw
青蛙过河
'''
from typing import List


class Solution:
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