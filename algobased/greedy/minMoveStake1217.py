class Solution:
    '''脑经急转弯, 贪心的思想
    移动最少的,奇数 偶数 谁数量少,就是最少. 细想'''
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd, even = 0, 0
        for p in position:
            if p % 2 == 0:
                odd += 1
            else:
                even += 1
        return min(odd, even)