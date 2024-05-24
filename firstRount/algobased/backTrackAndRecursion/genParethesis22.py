class Solution:
    '''
    经典背诵题
    回溯算法
    不撤销分支不一定不是回溯法
    这是因为每个分支都是一个新的str，你对当前分支的修改并不会影响到其他分支，所以并不需要撤销操作
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0 :
            return []
        res = []
        def dfs(left,right,path):
            if right * 2 == n:
                res.append(path)
                return
            if left < n :
                dfs(left + 1 , right, path + '(')
            if right < left:
                dfs(left, right + 1 , path + ')')

        dfs(0,0,'')
        return res

    def generateParenthesisBacktrack(self, n: int) -> List[str]:
        parentheses = []  # 存放所有括号组合
        parenthesis = []  # 存放当前括号组合

        def backtrack(symbol, index):
            if n * 2 == index:
                if symbol == 0:
                    parentheses.append("".join(parenthesis))
            else:
                if symbol < n:
                    parenthesis.append('(')
                    backtrack(symbol + 1, index + 1)
                    parenthesis.pop()
                if symbol > 0:
                    parenthesis.append(')')
                    backtrack(symbol - 1, index + 1)
                    parenthesis.pop()

        backtrack(0, 0)
        return parentheses