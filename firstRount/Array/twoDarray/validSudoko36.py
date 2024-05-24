import collections

from firstRount.LinkedList import List


# 经典题 学习了怎么在数组中找到小的cube的简便方法
# python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = collections.defaultdict(set)
        col_set = collections.defaultdict(set)
        cube_set = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if num in row_set[i] or num in col_set[j] or num in cube_set[(i//3,j//3)]:
                        return False
                    row_set[i].add(num)
                    col_set[j].add(num)
                    cube_set[(i//3,j//3)].add(num)

        return True


