
'''
https://github.com/doocs/leetcode/blob/main/solution/0600-0699/0694.Number%20of%20Distinct%20Islands/README.md
我们遍历网格中的每个位置
，如果该位置为
，则以其为起始节点开始进行深度优先搜索，过程中将
 修改为
，并且将搜索的方向记录下来，等搜索结束后将方向序列加入哈希表中，最后返回哈希表中不同方向序列的数量即可。
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, k: int):
            grid[i][j] = 0
            path.append(str(k))
            dirs = (-1, 0, 1, 0, -1)
            for h in range(1, 5):
                x, y = i + dirs[h - 1], j + dirs[h]
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    dfs(x, y, h)
            path.append(str(-k))

        paths = set()
        path = []
        m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    dfs(i, j, 0)
                    paths.add("".join(path))
                    path.clear()
        return len(paths)