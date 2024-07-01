'''
https://www.1point3acres.com/bbs/thread-1054159-1-1.html
题目是求2D数组里可以根据时间线拿的最多个订单数
'''
import collections

from firstRount.LinkedList import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        dfs + memo table
        if has visited before, end dfs
        dfs searching to 4 dirs, if any value is larger than current value, it is longest path increase 1
        store largest value from 4 directions in memo table of current pos
        '''
        if not matrix: return 0
        rows,cols = len(matrix),len(matrix[0])
        memo = [[0 for _ in range(cols)] for _ in range(rows)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(row,col):
            if memo[row][col] != 0: ## already visited
                return  memo[row][col]
            memo[row][col] = 1 ## default value is 1
            for dx, dy in dirs:
                newdx, newdy = row + dx, col + dy
                if 0<= newdx < rows and 0 <= newdy < cols and matrix[newdx][newdy] > matrix[row][col]:
                    memo[row][col] = max(memo[row][col],dfs(newdx,newdy) + 1)

            return memo[row][col]

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if memo[i][j] != 0:
                    ans = max(ans, memo[i][j])
                else:
                    ans = max(ans, dfs(i, j))

        return ans


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])

        # Topological Starting
        out_degrees = collections.defaultdict(list)
        in_degrees = collections.defaultdict(int)

        # gets all neighbors that are in bound
        def get_neighbors(i, j):
            for new_i, new_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= new_i < m and 0 <= new_j < n:
                    yield (new_i, new_j)

        # for each neighbor of a specific cell that is greater
        # than the specific cell gets out and in degree modified
        for i in range(m):
            for j in range(n):
                for new_i, new_j in get_neighbors(i, j):
                    if matrix[i][j] < matrix[new_i][new_j]:
                        out_degrees[(i, j)] += [(new_i, new_j)]
                        in_degrees[(new_i, new_j)] += 1

        # A cell with in-degree of 0 is a cell that is greater
        # than all its neighbors.
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if in_degrees[(i, j)] == 0:
                    queue.append((i, j))

        # Go through each level(in degree's with 0 first), and then decrement
        # the indegree for all the nodes the current node points to.
        # If that indegree then becomes 0 after decrement its ready to be
        # inserted to the next batch(level)
        # By each level increment the length
        max_len = 0
        while queue:
            max_len += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for new_coord in out_degrees[i, j]:
                    in_degrees[new_coord] -= 1
                    if in_degrees[new_coord] == 0:
                        queue.append(new_coord)

        return max_len