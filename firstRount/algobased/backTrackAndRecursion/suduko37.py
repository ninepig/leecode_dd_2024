class solution
'''太经典的backtrack题'''
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.backtrack(board)

    def backtrack(self, board):
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                for k in range(1,10):
                    if self.isValid(i,j,k,board):
                        board[i][j] = str(k)
                        if self.backtrack(board):
                            return True
                        board[i][j] = '.'
                return False
        return True

    def isValid(self, row, col, k, board):
        for i in range(9):
            if board[i][col] == k:
                return False
        for j in range(9):
            if board[row][j] == k:
                return  False

        row_start = row // 3 * 3
        col_start = col // 3 * 3
        for i in range(row_start,row_start + 3):
            for j in range(col_start , col_start + 3):
                if board[i][j] == k :
                    return False
        return True

class Solution:
    def backtrack(self, board: List[List[str]]):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    continue
                for k in range(1, 10):
                    if self.isValid(i, j, k, board):
                        board[i][j] = str(k)
                        if self.backtrack(board):
                            return True
                        board[i][j] = '.'
                return False
        return True

    def isValid(self, row: int, col: int, val: int, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            if board[row][i] == str(val):
                return False

        for j in range(0, 9):
            if board[j][col] == str(val):
                return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(val):
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.backtrack(board)
        """
        Do not return anything, modify board in-place instead.
        """
