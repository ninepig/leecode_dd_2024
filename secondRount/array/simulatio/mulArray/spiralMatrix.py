from typing import List


'''经典模拟题
利用四个flag 来做
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        up,left,right,down =0,0,col-1,row-1
        res = []
        while True:
            ## left to right
            for i in range(left,right + 1): ## + 1 since we need right
               res.append(matrix[up][i])
            up += 1
            if up > down:
                break
            ## top to down
            for i in range(up,down + 1):
                res.append(matrix[i][right])## bug, [i][right] not [right][i]
            right -= 1

            if right < left:
                break
            ## right to left
            for i in range(right,left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
            if down < up:
                break

            ## down to top
            for i in range(down,up - 1,-1):
                res.append(matrix[i][left]) ## bug, [i][left] not [left][i]
            left += 1
            if left > right:
                break

        return res


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        index = 1
        while True:
            for i in range(left, right + 1):
                matrix[up][i] = index
                index += 1
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                matrix[i][right] = index
                index += 1
            right -= 1
            if right < left:
                break
            for i in range(right, left - 1, -1):
                matrix[down][i] = index
                index += 1
            down -= 1
            if down < up:
                break
            for i in range(down, up - 1, -1):
                matrix[i][left] = index
                index += 1
            left += 1
            if left > right:
                break
        return matrix
