class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ''' 先把边边和靠着边边的o 变成# 然后第二次遍历的时候 # 变成o 别的地方的o变成x'''
        if not board:
            return
        m = len(board)
        n = len(board[0])

        def dfs(x,y):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != '0':
                return
            board[x][y] = '#'
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)

        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'o'
                if board[i][j] == 'o':
                    board[i][j] = 'x'

        return board