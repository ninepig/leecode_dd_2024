class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = dict()
        dirctions = [(1,0),(-1,0),(0,1),(0,-1)]
        mod = 10 ** 9 + 7
        def dfs(row,col,step):
            if row < 0 or col < 0 or row >= m or col >=n:
                return 1
            if step == 0: # 这个结束条件比较正确， 因为当你的步数已经0的时候就停止递归了
                return 0
            res = 0
            if (row,col) in memo:
                return memo[(row,col,step)]

            for dirct in dirctions:
                x = dirct[0]
                y = dirct[1]
                new_row = x + row
                new_col= y + col
                res += dfs(new_row,new_col,step - 1)
                res %= mod

            memo[(row,col,step)] = res

            return res

        return dfs(startRow,startColumn,maxMove)

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = dict()
        dirctions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        mod = 10 ** 9 + 7
        def dfs(row, col, step):
            if row < 0 or col < 0 or row >= m or col >= n:
                return 1
            if step == maxMove: # 没必要递归下去了 因为超过下一步就会超过最大
                return 0

            res = 0
            if (row, col) in memo:
                return memo[(row, col)]

            for dirct in dirctions:
                x = dirct[0]
                y = dirct[1]
                new_row = x + row
                new_col = y + col
                res += dfs(new_row, new_col, step + 1)
                res %= mod

            memo[(row, col)] = res

            return res

        return dfs(startRow, startColumn, 0)


## 完全正确的方法， 应该是我dict的问题？
## 对于这个题 ，memo的dict 是（row，col，step）这三个元组组成的， 因为不同的step到达这里会有不同的值。 这个ans是可能的数值
#所以还是要多做题，多写出递归的可能性
##更好的优化方法 就是数组替换 hash表

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        mod = 10 ** 9 + 7

        memo = [[[-1 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]

        def dfs(i, j, moveCount):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1

            if moveCount == 0:
                return 0

            if memo[i][j][moveCount] != -1:
                return memo[i][j][moveCount]

            ans = 0
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                ans += dfs(new_i, new_j, moveCount - 1)
                ans %= mod

            memo[i][j][moveCount] = ans
            return ans

        return dfs(startRow, startColumn, maxMove)
