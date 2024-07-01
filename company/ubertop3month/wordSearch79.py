class Solution:
    '''
    basic dfs
    '''
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        def dfs(row,col,index):
            if index == len(word) - 1:
                return True
            if board[row][col] == word[index]:
                visited[row][col] = True
                for dir in dirs:
                    new_row = row + dir[0]
                    new_col = col + dir[1]
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if dfs(new_row,new_col,index + 1):
                            return True
                visited[row][col] = False
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False