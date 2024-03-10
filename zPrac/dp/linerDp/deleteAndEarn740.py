'''
https://leetcode.cn/problems/delete-and-earn/solutions/758623/gong-shui-san-xie-zhuan-huan-wei-xu-lie-6c9t0
其实是rob的变种题
state --> dp[i][0]代表 i这个数值不选的最大值 dp[i][1]代表i这个数值 选的最大值
state inital -->dp[i][0]---dp[i][1] == 0
--->状态转移
对于选择i这个数--》 dp[i][1] = dp[i-1][0] + cnt[i] * i
对于不选择i这个数 --》 dp[i][0] = max(dp[i-1][0],dp[i-1][1])
数据范围 1---10001 所以可以利用一个count来做
太牛逼了 这个方法。。
'''
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = [0] * 10010
        max_number = 0
        for num in nums:
            count[num] += 1
            max_number = max(max_number,num)

        dp = [[0]*2 for _ in range(max_number + 1)]

        ## dp[max_number][x] is our target, so dp size is max_number + 1
        for i in range(1,max_number + 1):
            dp[i][1] = dp[i-1][0] + i*count[i]
            dp[i][0] = max(dp[i-1][1],dp[i-1][0])

        return max(dp[max_number][1],dp[max_number][0])# 加不加最后一个数
