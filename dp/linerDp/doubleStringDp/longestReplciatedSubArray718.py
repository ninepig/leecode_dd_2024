class Solution:
    '''双串dp'''
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # define state
        ans = 0
        num1_size = len(nums1)
        num2_size = len(nums2)
        # 以i j 为结束子串 最长的公共子数组数
        dp = [[0 for _ in range(num1_size + 1)]for _ in range(num2_size + 1 )]
        # initial done --》 初始都为0
        #状态转移 只有两数相等， dp【i][j]才能+1  否则 dp[i][j] 为0 不发生转移
        for i in range(1,num1_size):
            for j in range(1,num2_size):
                if nums2[j-1] == nums1[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                ans = max(ans,dp[i][j])
        # final state, 最大的值
        return ans
