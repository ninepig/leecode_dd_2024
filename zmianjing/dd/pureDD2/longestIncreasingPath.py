'''
这道题就是套皮329
它实际上会说一个出餐order
如何拿最多的order
memo + dfs
不需要backtrack
https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/solutions/944399/tong-ge-lai-shua-ti-la-yi-ti-si-jie-bfs-agawl

'''
class Solution:
    def longestPrepareOrder(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[0 for _ in range(rows)] for _ in range(cols)] #memo record node's presenting length
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        ''' searching ending 
        1 in memo, already visited 
        2 out of bound 
        3 not increasing 
        '''
        def dfs(row,col):
            if memo[row][col] != 0 : # visited
                return memo[row][col]

            cur = 1
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if (0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]):
                    cur = max(cur,dfs(new_row,new_row) + 1)  # get largest for 4 direction

            memo[row][col] = cur

            return cur

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if memo[i][j] == 0:
                    ans = max(ans,dfs(i,j))

        return ans