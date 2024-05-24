from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # step 1 reverse up & down
        for i in range(len(matrix)//2):
            for j in range(len(matrix[0])):
                matrix[i][j],matrix[len(matrix) - 1 - i] = matrix[len(matrix) - 1 - i],matrix[i][j]

        # step 2 reverse diagnoal
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
