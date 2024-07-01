from typing import List


class Solution:
    '''这道题状态方程很巧妙！ 答案错的~ 对dp长度的判断我没有错~ ^_^
    https://algo.itcharge.cn/10.Dynamic-Programming/03.Linear-DP/02.Linear-DP-02/#_4-2-%E6%9C%80%E5%A4%A7%E6%AD%A3%E6%96%B9%E5%BD%A2
    对于边上的1 ，dp 初始化为 1 ，
    状态转移
    如果 当前点是 1 --》 四个边必须都不为0才可以组成正方形。 仔细想想 非常牛逼
    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1'''
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = matrix[0][0]
        res = 0
        for i in range(rows):
            if matrix[i][0] == 1:
                dp[i][0] = 1
        for j in range(cols):
            if matrix[0][j] == 1:
                dp[0][j] = 1
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1
                    res = max(dp[i][j],res)

        return res * res

  # def maximalSquareBetterAnswer(self, matrix: List[List[str]]) -> int:
  #       rows, cols = len(matrix), len(matrix[0])
  #       max_size = 0
  #       dp = [[0 for _ in range(cols )] for _ in range(rows)]
  #       for i in range(rows):
  #           for j in range(cols):
  #               if matrix[i][j] == '1':
  #                   if i == 0 or j == 0:
  #                       dp[i][j] = 1
  #                   else:
  #                       dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
  #                   max_size = max(max_size, dp[i][j])
  #       return max_size * max_size