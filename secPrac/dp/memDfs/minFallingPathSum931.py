from cmath import inf
from functools import cache


class Solution:

    '''
    https://leetcode.cn/problems/minimum-falling-path-sum/solutions/2341851/cong-di-gui-dao-di-tui-jiao-ni-yi-bu-bu-2cwkb
    这道题就是 从上到下的 dfs + mem table 比较简单
    因为转移方程比较直接
    value[i][j] = min( value[i-1][j] , value [i-1][j-1], value[i-1][j+1])
    '''
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        @cache # memorization
        def dfs(r:int,c:int)->int:
            if c < 0 or c >= n :
                return inf
            if r == 0 : ## reach first line
                return matrix[0][c] ## return first column's value
            return min(dfs(r-1,c-1),dfs(r-1,c),dfs(r-1,c+1)) + matrix[r][c]

        res = 0
        for i in range(n):
            res = min(res,dfs(n-1,i)) # dfs from each column last row
        return res

        '''dp way'''
        def minFallingPathSumBottomup(self, matrix: List[List[int]]) -> int:
            n = len(matrix)
            f = [[inf] * (n + 2) for _ in range(n)]
            f[0][1: n + 1] = matrix[0]
            for r in range(1, n):
                for c in range(n):
                    f[r][c + 1] = min(f[r - 1][c], f[r - 1][c + 1], f[r - 1][c + 2]) + matrix[r][c]
            return min(f[-1])
