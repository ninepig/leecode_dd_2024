'''
仿真模拟题
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        top , bottom , left , right = 0, len(matrix) - 1 , 0, len(matrix[0]) - 1
        index = 0
        while True:
            for i in range(left, right + 1):
                matrix[top][i] = index
                index += 1
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom + 1):
                matrix[i][right] = index
                index += 1
            right -= 1
            if right < left:
                break

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = index
                index+=1
            bottom -= 1
            if bottom < top:
                break

            for i in range(bottom,top - 1 , -1):
                matrix[i][left] = index
                index+=1
            left+= 1
            if left > right :
                break

        return matrix
