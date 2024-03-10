'''
dp[n] means max money we can rob to nth house
dp[0] = num[0] dp[1] = num[1]
transfer => dp[n] = max(dp[n-1], dp[n-2] + num[n]

'''
class Solution:
    '''
    2种做法 都可以， 但一个dp的size 原数组长度 一个是 数组长度+1
    定义完全不一样。、
    '''
    ## 这个做法有些case不过
    # def rob(self, nums: List[int]) -> int:
    #     size = len(nums)
    #     if size <= 2:
    #         return max(nums)
    #     dp = [0] * size
    #     dp[0] = nums[0]
    #     dp[1] = nums[1]
    #     for i in range(2,size):
    #         dp[i] = max(dp[i - 2] + nums[i], dp[i-1])
    #
    #     return dp[size - 1]

    # 这里就是典型的 因为dp 的长度多1 所以 num 必须是-1 的题
    # dp 应该满足状态 ， 因为这里的dp[0]肯定是0 要到达第n间屋子 必须是dp[size+1]的数组才可以 这样才可以做到dp[size]
    # 到i间屋子所能偷窃到最大的金额 --》 这个时候能偷最多的就是i-1 个屋子 对于num数组 就是num[i-1]
    # 偷到i-1 间屋子 --》 2种  1 不偷 i-2 间屋子  所以 就是偷盗i-2之前的值 + num[i-1] 2 只偷到达i-1最大的房子
    # 画图出来做， 这里的i 是dp的序号， 在num之中 要-1 才能match
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0

        dp = [0 for _ in range(size + 1)]
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, size + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

        return dp[size]

    # 头尾相连， 所以只能偷 0--n-2 或者 1到n-1 家 比较大小
    def rob2(self,nums:List[int])-> int:
        size = len(nums)
        if size == 0 :
            return 0
        res_without_last = self.rob(nums[:size - 1])
        res_without_first =self.rob(nums[1:])
        return max(res_without_first,res_without_last)