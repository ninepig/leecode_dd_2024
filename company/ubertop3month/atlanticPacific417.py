from typing import List


class Solution:
    '''变形成为 从两侧出发，看看最高能到达的点，最后两个数组都能到达的点'''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = [[False for _ in range(n)] for _ in range(m)]
        alantic = [[False for _ in range(n)] for _ in range(m)]
        directory = [(0,1),(0,-1),(-1,0),(1,0)]

        def dfs(i,j,visited):
            visited[i][j] = True
            for direct in directory:
                new_i = i + direct[0]
                new_j = j + direct[1]
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n :
                    continue
                if  heights[new_i][new_j] >= heights[i][j] and not visited:
                    dfs(new_i,new_j,visited)

        for i in range(m):
            dfs(i,0,pacific)
            dfs(i,n-i,alantic)

        for j in range(n):
            dfs(0,j,pacific)
            dfs(m-1, j , alantic)

        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and alantic[i][j]:
                    res.append([i,j])

        return res


    def pacificAtlantic2(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        starting from pac/alt boarder.
        if neigher value is bigger than current, we can move forward , simulation water's flow
        check if a grid can be visit by pac/alt , then that is
        '''
        rows , cols = len(heights),len(heights[0])
        pac_visited = [[False for _ in range(cols)]for _ in range(rows)]
        alt_visited = [[False for _ in range(cols)]for _ in range(rows)]
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        def dfs(row,col,visited):
            visited[row][col] = True
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if not(0 <= new_row < rows and 0 <= new_col < cols):
                    continue ## out of box
                if not visited[new_row][new_col] and heights[new_row][new_col] > heights[row][col]:
                    dfs(new_row,new_col,visited)

        for i in range(rows):
            dfs(i,0,pac_visited)
            dfs(i,cols - 1 ,alt_visited)

        for i in range(cols):
            dfs(0,i,pac_visited)
            dfs(rows - 1 , i , alt_visited)

        res = []
        for i in range(rows):
            for j in range(cols):
                if pac_visited[i][j] and alt_visited[i][j]:
                    res.append([i,j])

        return res
