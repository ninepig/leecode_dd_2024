'''
标准的 dfs + memo 回溯法的题
https://leetcode.cn/problems/word-break-ii/solutions/468979/python3ji-yi-hua-sou-suo-tian-jia-3xing-dai-ma-1ge
'''
class Solution:
    # 超时
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        #
        wordDict = set(wordDict)

        def dfs(wordDict, temp, pos):
            #
            if pos == len(s):
                res.append(" ".join(temp))
                return
            for i in range(pos, len(s) + 1):
                if s[pos:i] in wordDict:
                    temp.append(s[pos:i])
                    dfs(wordDict, temp, i)
                    temp.pop()
                    #

        dfs(wordDict, [], 0)
        return res


    def wordBreakMem(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        memo = [1] * (len(s) + 1)
        wordDict = set(wordDict)

        def dfs(wordDict, temp, pos):
            num = len(res)  # 回溯前先记下答案中有多少个元素
            if pos == len(s):
                res.append(" ".join(temp))
                return
            for i in range(pos, len(s) + 1):
                if memo[i] and s[pos:i] in wordDict:  # 添加备忘录的判断条件
                    temp.append(s[pos:i])
                    dfs(wordDict, temp, i)
                    temp.pop()
            # 答案中的元素没有增加，说明s[pos:]不能分割，修改备忘录
            memo[pos] = 1 if len(res) > num else 0

        dfs(wordDict, [], 0)
        return res


    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)
        def dfs(path,pos):
            if pos == len(s): ## reach to the end of s
                res.append(" ".join(path))

            for i in range(pos, len(s) + 1):
                if s[pos:i] in wordDict:
                    path.append(s[pos:i])
                    dfs(path,i)
                    path.pop()
        return dfs([],0)
