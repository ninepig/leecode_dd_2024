class Solution:
    '''dfs + memo'''
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix :
            return 0
        max_length = 0
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        record = [[0 for _ in range(rows)] for _ in range(cols)]
        def dfs(row,col):
            nonlocal max_length
            record[row][col] = 1 # 利用1 表示visited 过了
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    if record[new_row][new_col] == 0: # not visited
                        dfs(new_row,new_col)
                    #改写当前record最大值
                    record[row][col] = max(record[row][col],record[new_row][new_col] + 1)
                max_length = max(max_length,record[row][col])
        for i in range(rows):
            for j in range(cols):
                if record[i][j] == 0:
                    dfs(i,j)
        return max_length