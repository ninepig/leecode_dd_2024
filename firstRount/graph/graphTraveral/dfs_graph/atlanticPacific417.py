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