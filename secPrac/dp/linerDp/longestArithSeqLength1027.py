'''这道题就是个枚举
对于dp 开窍了 看那个灵山的说法 非常对
子问题： 要么选 要不不选 或者就是枚举
其实就是暴力法
对于这个等差数列， 我们就是不断取差值

dp[i][j] 表示 以i结尾， j为差值的 最长数列的长度

https://leetcode.cn/problems/longest-arithmetic-subsequence/solutions/2239444/python3javacgotypescript-yi-ti-yi-jie-do-h9lz

https://leetcode.cn/problems/longest-arithmetic-subsequence/solutions/2239191/ji-yi-hua-sou-suo-di-tui-chang-shu-you-h-czvx
对于动态规划问题，通常可以从「选或不选」和「枚举选哪个」这两个角度入手。

看到子序列，你可能想到了「选或不选」这个思路，但是本题要寻找的是等差子序列，假设我们确定了等差子序列的末项和公差，那么其它数也就确定了，所以寻找等差子序列更像是一件「枚举选哪个」的事情了。

'''
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        size = len(nums)
        res = 1
        # 1001 means range from 0 --- 1000 for diff
        # inital dp[i][j] = 1  since every one can get 1 for arith array
        dp = [[1] * 1001 for _ in range(size)]
        for i in range(1,size):
            # 枚举每一个的等差
            for k in range(i):
                diff = nums[i] - nums[k] + 500 # avoid out of floor , since diff can be -500---500 --> 0 --- 1000
                dp[i][diff] = max(dp[i][diff],dp[k][diff])
                res = max(res, dp[i][diff])

        return res

