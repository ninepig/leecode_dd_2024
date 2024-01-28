class Solution:
    '''记忆化的经典题. 记忆化其实就是 hashtable + dfs  自顶向下'''
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = [[[-1 for _ in range(maxMove)] for _ in range(m)] for _ in range(n)]
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        def dfs(row,col,stepLeft):
            if row < 0 or row >=m or col < 0 or col >= n:
                return 1 # out of bound
            if stepLeft == 0 :
                return 0 # no more step
            if memo[row][col][stepLeft] != -1: # have visit
                return memo[row][col][stepLeft]

            ans = 0

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                ans += dfs(new_row,new_col,stepLeft - 1)
                ans = ans % 111
            # memo process
            memo[row][col][stepLeft] = ans


        return dfs(startRow,startColumn,maxMove)

