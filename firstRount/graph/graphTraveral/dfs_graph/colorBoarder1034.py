class solution:
    '''
    要求：对起始位置 (row, col) 所在的连通分量边界填充颜色为 color。并返回最终的二维整数矩阵 grid
    只在边界填充颜色,题目不是很清晰 我觉得不会考
    '''
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        m = len(grid)
        n = len(grid[0])
        #遍历题 利用visited数组增加效率
        visited = [[False for _ in range(n)] for _ in range(m)]
        def dfs(i,j):
            for direct in direction:
                new_i = i + direct[0]
                new_j = j + direct[1]
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    # 到边界了,染色
                    grid[i][j] = color
                if visited[new_i][new_j]:
                    return
                if grid[new_i][new_j] == grid[i][j]: # 颜色相同
                    visited[new_i][new_j] = True
                    dfs(new_i,new_j)
                else:
                    #颜色不同 染色
                    grid[i][j] = color
        dfs(0,0)
        return grid