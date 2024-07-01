'''模拟题
因为下一个状态会被当前状态影响，所以 不能以0 ， 1 作为计数， 因为不能用多余的matrix
所以需要用中间状态， 比如-1 ， 2 这样的数字。 用以更新下一个状态'''


def countNeigher(directions, i, j, board,rows,cols):
    count = 0
    for x,y in directions:
        new_x = i + x
        new_y = j + y
        if 0<= new_x< rows and 0 <= new_y <= cols and board[new_x][new_y] == 1:
            count += 1
    return count


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 8 direction
        directions = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]
        rows = len(board)
        cols = len(board[0])
        # current state affect next state
        for i in range(rows):
            for j in range(cols):
                neighlife = countNeigher(directions, i, j, board, rows, cols)
                if board[i][j] == 1:
                    if neighlife < 2 or neighlife>3:
                        board[i][j] = -1
                if board[i][j] == 0:
                    if neighlife == 3:
                        board[i][j] = 2
        # next state
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1

