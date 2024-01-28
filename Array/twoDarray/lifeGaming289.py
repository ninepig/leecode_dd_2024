'''
很好的模拟仿真题
因为不能增加额外的空间
所以inplace change
利用的是
死细胞 -> 死细胞，活细胞 -> 活细胞，不会对前后状态造成影响，所以主要考虑另外两种情况。我们把活细胞 -> 死细胞暂时标记为
，并且统计每个细胞周围活细胞数量时，使用绝对值统计，这样
 也可以暂时标记为活细胞。然后把死细胞 -> 活细胞暂时标记为
，这样判断的时候也不会统计上去。然后开始遍历。

遍历二维数组的每一个位置。并对该位置遍历周围八个位置，计算出八个位置上的活细胞数量。
如果此位置是活细胞，并且周围活细胞少于
 个或超过
 个，则将其暂时标记为
，意为此细胞死亡。
如果此位置是死细胞，并且周围有
 个活细胞，则将暂时标记为
，意为此细胞复活。
遍历完之后，再次遍历一遍二维数组，如果该位置为
，将其赋值为
，如果该位置为
，将其赋值为
。

'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 8 directions
        directions = {(1,0),(-1,0),(0,-1),(0,1),(1,-1),(-1,-1),(1,1),(-1,1)}
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                ## count every 8 neighbours
                live = 0
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]

                    if 0<= new_row < row and 0 <= new_col < col and abs(board[new_row][new_col]) == 1:
                        live += 1
                if board[row][col] == 1 and (live < 2 or live > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and (live == 3):
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                if board[row][col] == 2:
                    board[row][col] = 1

