from typing import List

'''
设定两个变量 flag_row0、flag_col0 来标记第一行、第一列是否出现了 0。

接下来我们使用数组第一行、第一列来标记 0 的情况。

对数组除第一行、第一列之外的每个元素进行遍历，如果某个元素出现 0 了，则使用数组的第一行、第一列对应位置来存储 0 的标记。

再对数组除第一行、第一列之外的每个元素进行遍历，通过对第一行、第一列的标记 0 情况，进行置为 0 的操作。

然后再根据 flag_row0、flag_col0 的标记情况，对第一行、第一列进行置为 0 的操作。
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        first_row_flag = False
        first_col_flag = False
        # CHECK IF first row/col has 0
        for i in range(n):
            if matrix[i][0] == 0:
                first_col_flag = True
                break
        for i in range(m):
            if matrix[0][i] == 0:
                first_row_flag = True
                break
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 0:
                    matrix[i][0] , matrix[0][j] = 0 , 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0 :
                    matrix[i][j] = 0

        if first_row_flag :
            for i in range(n):
                matrix[0][i] = 0

        if first_col_flag :
            for i in range(m):
                matrix[i][0] = 0

