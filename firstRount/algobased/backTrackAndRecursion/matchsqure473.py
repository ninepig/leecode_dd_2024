"""
先排除数组为空和火柴总长度不是 4 的倍数的情况，直接返回 False。
然后将火柴按照从大到小排序。用数组 sums 记录四个边长分组情况。
将火柴分为 4 组，把每一根火柴依次向 4 条边上放。
直到放置最后一根，判断能否构成正方形，若能构成正方形，则返回 True，否则返回 False。


wenjing : 四条边的backtrack 经典好题
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks: return False
        size = len(matchsticks)
        sum_len = sum(matchsticks)
        if sum_len % 4 != 0:
            return False
        sidelen = sum_len / 4
        matchsticks.sort(reverse = True) # order from big to small
        match_sum = [ 0 for _ in range(4)]
        return self.dfs(0,match_sum,matchsticks,size,sidelen)

    def dfs(self, index, match_sum, matchsticks, size, sidelen):
        # 所有火柴全部被使用了
        if index == size:
            return True
        # make 4 side has equal value
        for i in range(4):
            if i > 0 and match_sum[i] == match_sum[i-1]:
                continue
            match_sum[i] += matchsticks[index]
            if sum[i] <= sidelen and self.dfs(index + 1, match_sum,matchsticks,size,sidelen):
                return True
            match_sum[i] -= matchsticks[index]

        return False


class SolutionAnswer:
    def dfs(self, index, sums, matchsticks, size, side_len):
        if index == size:
            return True

        for i in range(4):
            # 如果两条边的情况相等，只需要计算一次，没必要多次重复计算
            if i > 0 and sums[i] == sums[i - 1]:
                continue
            sums[i] += matchsticks[index]
            if sums[i] <= side_len and self.dfs(index + 1, sums, matchsticks, size, side_len):
                return True
            sums[i] -= matchsticks[index]

        return False

    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        size = len(matchsticks)
        sum_len = sum(matchsticks)
        if sum_len % 4 != 0:
            return False

        side_len = sum_len // 4
        matchsticks.sort(reverse=True)

        sums = [0 for _ in range(4)]
        return self.dfs(0, sums, matchsticks, size, side_len)