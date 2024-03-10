class Solution:
    '''状态转移方程 两种情况'''
    def numDecodings(self, s: str) -> int:
        ##
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1 # 0 we have 1 menthod to decode --> null

        for i in range(1,len(s) + 1) :
            if s[i - 1] != '0':
                ## 使用一个字符，取决于 i-1 有多少种方法
                dp[i] += dp[i-1]
            if i > 0 and s[i-2] != '0'  and int(s[i-2:i]) <=  26:
                ## 使用了2个字符， 取决于 i-2 有多少种解
                dp[i] += dp[i-2]

        return dp[len(s)]