from typing import List


class solution:
    ## 标准的模拟题， 一定要画图 然后归纳。 没做过应该也能做出来
    ## //1 + 2 = clockwise rotation
    # //1 + 3 = anti-clockwise rotation
    # //2 + 3 = 180 degree rotation
    def rotate(self, matrix: List[List[int]]) -> None:
        ## 先垂直反转 再 对角线反转
        if not matrix or len( matrix ) == 0 : return
        n = len(matrix)

        ## 正向对角线反转
        for i in range(n):
            for j in range(i):
                matrix[i][j] , matrix[j][i] = matrix[j][i],matrix[i][j]

        ## 垂直反转
        for i in range(n//2):
            for j in range(n):
                matrix[i][j],matrix[n - i - 1][j] = matrix[n-i-1][j] , matrix[i][j]

        ##水平翻转
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]

