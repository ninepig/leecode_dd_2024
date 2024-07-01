class solution:

    def isvalid(self, row, col, c, grid):
        for i in range(len(grid)):
            if grid[row][i] == c:
                return False
            if grid[i][col] == c:
                return False
            if grid[(3 * (row // 3) + i // 3)][3 * (col // 3) + i % 3] == c:
                return False
        return True

    def solveSudoku(self, grid: list[list[str]]) -> None:
        return self.solve(grid)

    def solve(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ".":
                    for c in range(1, len(grid) + 1):
                        c = str(c)
                        if self.isvalid(i, j, c, grid):
                            grid[i][j] = c
                            if self.solve(grid) == True:
                                return True
                            else:
                                grid[i][j] = "."
                    return False
        return True
'''经典hash表题
核心是这个box index的算法'''


def isValidSudoku(self, board: list[list[str]]) -> bool:
    row_maps = [dict() for _ in range(9)]
    col_maps = [dict() for _ in range(9)]
    box_maps = [dict() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            # 关键算法
            num = int(board[i][j])
            box_index = (i // 3) * 3 + j // 3
            row_value = row_maps[i].get(num, 0)
            col_value = col_maps[j].get(num, 0)
            box_value = box_maps[box_index].get(num, 0)
            if row_value > 0 or col_value > 0 or box_value > 0:
                return False
            row_maps[i][num] = 1
            col_maps[j][num] = 1
            box_maps[box_index][num] = 1

    return True




