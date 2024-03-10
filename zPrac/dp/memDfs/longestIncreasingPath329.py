class Solution:
    '''经典dfs + memo
    https://algo.itcharge.cn/Solutions/0300-0399/longest-increasing-path-in-a-matrix/#%E4%BB%A3%E7%A0%81
    利用memo 每次dfs 都先把访问过的记录下来。
    这道题里 dfs 其实就是访问，不需要做什么特别的操作， 所以就是在访问的过程之中 更新最大值'''
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        def dfs(row , col):
            global res
            memo[row][col] = 1
            for dir in directions:
                new_r = row + dir[0]
                new_c = col + dir[1]
                if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]) and matrix[new_r][new_c] > matrix[row][col] : # > 代表递增  》= 也可以是
                    if memo[new_r][new_c] == 0: # 没访问过的 直接dfs访问，要不然就直接加1
                        dfs(new_r,new_c)
                    memo[row][col] = matrix(memo[row][col], memo[new_r][new_c] + 1)
            # 四个方向都走完 ，就统计当前节点最大的path
            res = max(memo[row][col],res)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if memo[i][j] == 0:
                    dfs(i,j)
        return res