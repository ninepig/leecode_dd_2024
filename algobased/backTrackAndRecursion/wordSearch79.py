class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ## 结束条件 长度相同，最后一位等于目标位
        # 递进条件： 每一位的值等于目标位
        # 利用visited table 来剪枝 后退
        # 有true/false的backtrack 多用他放在判断条件之中
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        length = len(board)
        width = len(board[0])
        visited = [[False for i in range(width)] for i in range(length)]
        def backtrack(index,row,col):
            if index == len(word) - 1:
                return board[row][col] == word[index]
            if board[row][col] == word[index]:
                visited[row][col] = True
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if 0<= new_row < length and 0 <= new_col < width and visited[new_row][new_col] == False and backtrack(index + 1 , new_row,new_col):
                        return True
                visited[row][col] = False
            return False
        for i in range(length):
            for j in range(width):
                if backtrack(0,i,j):
                    return True

        return False

class SolutionAns:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(board)
        if rows == 0:
            return False
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def backtrack(i, j, index):
            if index == len(word) - 1:
                return board[i][j] == word[index]

            if board[i][j] == word[index]:
                visited[i][j] = True
                for direct in directs:
                    new_i = i + direct[0]
                    new_j = j + direct[1]
                    if 0 <= new_i < rows and 0 <= new_j < cols and visited[new_i][new_j] == False:
                        if backtrack(new_i, new_j, index + 1):
                            return True
                visited[i][j] = False
            return False

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False