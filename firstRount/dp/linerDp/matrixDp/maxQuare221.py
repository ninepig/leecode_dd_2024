class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix),len(matrix[0])
        # state dp[i][j] means end with i, j 's largest length of squre's side
        dp =[[0 for _ in range(rows)] for _ in range(cols)]

        # inital
        # TODO 这里应该是错的?
        for i in range(rows):
            if matrix[i][0] == 1:
                dp[i][0] = 1

        for i in range(cols):
            if matrix[0][i] == 1:
                dp[0][i] = 1
        res = 0
        # state transfer
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                #dp[i][j]由上方、左侧、左上方三者共同约束的，为三者中最小值加
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    res = max(res,dp[i][j])

        return res * res

    # 不知道为什么我的不对..傻逼oj. 下面这是对的
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        max_size = 0
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    max_size = max(max_size, dp[i][j])
        return max_size * max_size

