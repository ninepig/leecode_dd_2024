from firstRount.LinkedList import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if not s or len(s) == 0:
            return []
        res = []
        def backTrack(path,index):
            if index == len(s):
                res.append(path)
                return
            ## normal case
            backTrack(path + s[index], index + 1)
            ## lower -> upper
            if ord('a') <= ord(s[index]) <= ord('z'):
                backTrack(path + str.upper(s[index]), index + 1)
            if ord('A') <= ord(s[index]) <= ord('Z'):
                backTrack(path + str.upper(s[index]), index + 1)
        backTrack('',0)
        return res

class Solution:
    def dfs(self, s, path, i, ans):
        if i == len(s):
            ans.append(path)
            return

        self.dfs(s, path + s[i], i + 1, ans)
        if ord('a') <= ord(s[i]) <= ord('z'):
            self.dfs(s, path + s[i].upper(), i + 1, ans)
        elif ord('A') <= ord(s[i]) <= ord('Z'):
            self.dfs(s, path + s[i].lower(), i + 1, ans)

    def letterCasePermutation(self, s: str) -> List[str]:
        ans, path = [], ""
        self.dfs(s, path, 0, ans)
        return ans