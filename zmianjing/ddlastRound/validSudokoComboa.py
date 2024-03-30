from collections import defaultdict


class Sudoku:
    ## 关键还是如何locate matrix  这样比较简单。 锁定9个小盒子。 用defaultDict来做 然后对于 （i//3,j//3) 这个形式比较好
    def validSudoko(self,board:list[[int]]):
        row_bag = defaultdict(set)
        col_bag = defaultdict(set)
        sec_bag = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if not num.isdigit():
                    continue

                sec = (i // 3, j // 3)
                if num in row_bag[i] or num in col_bag[j] or num in sec_bag[sec]:
                    return False
                else:
                    row_bag[i].add(num)
                    col_bag[j].add(num)
                    sec_bag[sec].add(num)

        return True


    def isValid(self, row, col, c, grid):
        for i in range(9):
            if grid[row][i] == c :
                return False
            if grid[i][col] == c :
                return False
            if grid[row//3 * 3 + i//3][col//3*3 + i%3] == c:
                return False
        return True

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        return self.solve(board)

    def solve(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == '.':
                    for c in range(1,10):
                        c = str(c)
                        if self.isValid(i,j,c,grid): ## compare if row,col,box has that char
                            grid[i][j] = c
                            if self.solve(grid):
                                return True
                            ## backtrack必须是在这一层。。
                            else:
                                grid[i][j] = '.' ## backtrack
                    return False

        return True

