from functools import cache


class Solution:
    # 最基本的dfs + memo 方法
    def tribonacci(self, n: int) -> int:
        @cache
        def dfs(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2 :
                return 1

            return dfs(n-1)+dfs(n-2) + dfs(n-3)

        return dfs(n)
