'''
这道题太经典了
利用一个额外的状态 -1 来做
-1 1 的绝对值都是1 -1 不会影响下一个state的计算， 达到inplace的目的

这个题就是个模拟+脑经急转弯


'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = {(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)}

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                lives = 0
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    ## 关键是这个 abs 。。。没想到就真的想不到了
                    if 0 <= new_row < rows and 0 <= new_col < cols and abs(board[new_row][new_col]) == 1:
                        lives += 1
                if board[row][col] == 1 and (lives < 2 or lives > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and lives == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1
