'''
利用数组的第一行 第一列 来做计数
先看看第一行 第一列是否有0 ， 标记下来， 用来最后给第一行第一列是否全部需要置0
循环matrix ， 如果非第一行第一列 有0， 把第一行 第一列置为0 用来标记
循环matrix， 如果第一行 or第一列为0， 把i，j 置为 0
最后查看第一行第一列，是否需要全部置为0

技巧题

'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        row_0 = False
        col_0 = False

        # check if row_0 , col_0 true or False
        for i in range(rows):
            if matrix[i][0] == 0:
                row_0 = True
                break

        for j in range(cols):
            if matrix[0][j] == 0:
                col_0 = True
                break

        # record any 0 happen in which row,col
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # make matrix value to 0 if column or row = 0
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # check first row, first col

        if row_0:
            for i in range(cols):
                matrix[0][i] = 0
        if col_0:
            for i in range(rows):
                matrix[i][0] = 0


