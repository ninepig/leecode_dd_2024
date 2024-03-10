class Solution:
    '''
    这题 同样 dp的长度是 size + 1， 所以循环都要变成size+ 1 同时对于num 要取 i - 1
    dp[i][j] 以string i string j 结尾 的值
    状态转移 --》 只有num[i-1] == num2[j-1] --> dp[i][j] = dp[i-1][j-1] +1 其余 dp[i][j] = 0
    '''
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        size1 = len(nums1)
        size2 = len(nums2)
        res = 0
        dp = [[0 for _ in range(size2+1)] for _ in range(size1+1)]
        for i in range(size1 + 1):
            for j in range(size2 + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res,dp[i][j])

        return res

