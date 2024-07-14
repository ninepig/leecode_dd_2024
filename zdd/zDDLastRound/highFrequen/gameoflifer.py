
'''
follow up https://www.1point3acres.com/bbs/thread-907534-1-1.html
    ## 如果格子上有些restaurant是permanently open的，不受规则影响来open close，怎么改。
    # 并且要求output出哪些permanently open的店如果本来不是permanent的话会被关掉。这问也不难改，做完之后还剩20分钟，就提前结束开始聊天了
'''
import copy


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Any live cell with fewer than two live neighbors dies as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population.
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        """
        ## RC ##
        ## APPRAOCH : IN-PLACE MANIPULATION ##
        #  when the value needs to be updated, we donot just change  0 to 1 / 1 to 0 but we do in increments and decrements of 2. (table explains)
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
                    if (i + x < len(board) and i + x >= 0) and (j + y < len(board[0]) and j + y >= 0) and abs(
                            board[i + x][j + y]) == 1:
                        live += 1
                if board[i][j] == 1 and (live < 2 or live > 3):  # Rule 1 or Rule 3
                    board[i][j] = -1
                if board[i][j] == 0 and live == 3:  # Rule 4
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if (board[i][j] > 0) else 0
        return board


class SolutionExtraspace(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board and board[0]:
            M, N = len(board), len(board[0])
            board_next = copy.deepcopy(board)
            for m in range(M):
                for n in range(N):
                    lod = self.liveOrDead(board, m, n)
                    if lod == 2:
                        board_next[m][n] = 0
                    elif lod == 1:
                        board_next[m][n] = 1
            for m in range(M):
                for n in range(N):
                    board[m][n] = board_next[m][n]

        ## 如果格子上有些restaurant是permanently open的，不受规则影响来open close，怎么改。
        # 并且要求output出哪些permanently open的店如果本来不是permanent的话会被关掉。这问也不难改，做完之后还剩20分钟，就提前结束开始聊天了
        #             if(m,n) in xxxx 加一个map的判断就行了 不难

    def liveOrDead(self, board, i, j):  # return 0-nothing,1-live,2-dead
        ds = [(1, 1), (1, -1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1)]
        live_count = 0
        M, N = len(board), len(board[0])
        for d in ds:
            r, c = i + d[0], j + d[1]
            if 0 <= r < M and 0 <= c < N:
                if board[r][c] == 1:
                    live_count += 1
        if live_count < 2 or live_count > 3:
            return 2
        elif board[i][j] == 1 or (live_count == 3 and board[i][j] == 0):
            return 1
        else:
            return 0



