class SolutionBrutalForce:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n_rows = len(board)
        n_cols = len(board[0])

        def count_live_neighbors(x: int, y: int) -> int:
            count = 0
            neighbor_coordinates = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                                    (x, y - 1), (x, y + 1),
                                    (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
            for (nx, ny) in neighbor_coordinates:
                if 0 <= nx < n_rows and 0 <= ny < n_cols and board[nx][ny] == 1:
                    count += 1
            return count

        # Create a copy of the board to store the next state
        next_board = [[0] * n_cols for i in range(n_rows)]

        for i in range(n_rows):
            for j in range(n_cols):
                neighbor = count_live_neighbors(i, j)
                if board[i][j] == 1 and (neighbor == 2 or neighbor == 3):
                    next_board[i][j] = 1
                if board[i][j] == 0 and neighbor == 3:
                    next_board[i][j] = 1  # Mark as alive

        # Update the board based on marked cells
        for i in range(n_rows):
            for j in range(n_cols):
                board[i][j] = next_board[i][j]

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Any live cell with fewer than two live neighbors dies as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population.
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        """
        ## RC ##
        ## APPRAOCH : IN-PLACE MANIPULATION ##
        #  when the value needs to be updated, we donot just change  0 to 1 / 1 to 0
        #  but we do in increments and decrements of 2. (table explains)
        ##   previous value state change  current state   current value
        ##   0              no change     dead            0
        ##   1              no change     live            1
        ##   0              changed (+2)  live            2
        ##   1              changed (-2)  dead            -1

        ## TIME COMPLEXITY : O(MxN) ##
        ## SPACE COMPLEXITY : O(1) ##

        directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0  # live neighbors count
                for x, y in directions:  # check and count neighbors in all directions
                    ## we use abs value to judge, so -1 also means neighbour live node even if we change by rule1/3
                    if (i + x < len(board) and i + x >= 0) and (j + y < len(board[0]) and j + y >= 0) and abs(
                            board[i + x][j + y]) == 1:
                        live += 1
                #### 如果格子上有些restaurant是permanently open的，不受规则影响来open close，怎么改。
                ## 这里多个条件 如果是board[i][j] == 1 and in permenatMap()
                # 并且要求output出哪些permanently open的店如果本来不是permanent的话会被关掉。这问也不难改，做完之后还剩20分钟，就提前结束开始聊天
                '''
                if board[i][j] == 1 and (i,j) in permMap
                    board[i][j] = 1
                    if (live < 2 or live > 3):
                        shouldChange.append([i,j])
                '''
                if board[i][j] == 1 and (live < 2 or live > 3):  # Rule 1 or Rule 3
                    board[i][j] = -1
                if board[i][j] == 0 and live == 3:  # Rule 4
                    board[i][j] = 2
                ##rule 2 , does not change , so live to next
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if (board[i][j] > 0) else 0
        return board

## 如果格子上有些restaurant是permanently open的，不受规则影响来open close，怎么改。
# 并且要求output出哪些permanently open的店如果本来不是permanent的话会被关掉。这问也不难改，做完之后还剩20分钟，就提前结束开始聊天了