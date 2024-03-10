from functools import cache


class Solution:
    '''
    dp/ dfs + mom 两种做法
    dp --》
    dp[n] n长度 是否可以由 dict组成
    dp[0] true
    返回dp[n]
    https://leetcode.cn/problems/word-break/solutions/50986/dong-tai-gui-hua-ji-yi-hua-hui-su-zhu-xing-jie-shi
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        ## initial
        dp = [False] * (n+1) ## inital
        dp[0] = True
        for i in range(n):
            for j in range(i+1,n+1):
                # state transfer
                # if dp[j] = True if dp[i] = true and s[i:j] in dict, j from i + 1 to n (n+1)
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]

    def wordBreakDFS(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if (not s):
                return True
            res = False
            for i in range(1, len(s) + 1): # 从1开始，因为需要s[0:1) 来判断 s[0:0]就是空
                if (s[:i] in wordDict): # 太巧妙了
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)


'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        ## state : dp[n] means if length n's string can be formed by word in dict
        dp = [False] * (n+1)
        dp[0] = True # dp[0] can be form
        for i in range(n):
            for j in range(i+1,n + 1):
                if dp[i] and s[i:j] in wordDict: # if dp[i] is true, and string[i : j ) in wordDict : state transfer
                    dp[j] = True

        return dp[-1]

    def wordBreakMem(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        @cache # memorize table
        def dfs(target):
            if not target:
                return True
            res = False
            for i in range(1,n + 1):
                if s[:i] in wordDict : # if this exist in worddict
                    res = dfs(target[i:]) or res
            return res
        return dfs(s)
    #太牛逼了。。。

