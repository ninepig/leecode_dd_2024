'''
Given an integer matrix, find the length of the longest path that have same values. The matrix has no boundary limits. (like, Google Maps - see edit for context)

From each cell, you can either move to two directions: horizontal or vertical. You may NOT move diagonally or move outside of the boundary.

nums = [
[1,1],
[5,5],
[5,5]
]

Return 4 ( Four 5's).

这道题虽然说的是相同的value path，但实际上就是相同数的最大面积

https://leetcode.com/discuss/interview-question/392780/Doordash-or-Phone-Screen-or-Longest-path-duplicate-numbers-within-a-Matrix/656634

这个java 方法应该是对的 ，和max area 还是有点区别的

public class Main {

    static boolean[][] visited;
    private static int longestPath(int[][] matrix) {
        visited = new boolean[matrix.length][matrix[0].length];
        int longest = 0;

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                longest = Math.max(dfs(matrix, i, j), longest);
            }
        }
        return longest;
    }

    private static int dfs(int[][] matrix, int i, int j) {
        if (visited[i][j]) {
            return 0;
        }

        visited[i][j] = true;
        int down = 0;
        if (i+1 < matrix.length && matrix[i+1][j] == matrix[i][j]) {
            down = dfs(matrix, i+1, j);
        }
        int up = 0;
        if (i-1 >=0 && matrix[i-1][j] == matrix[i][j]) {
            up = dfs(matrix, i-1, j);
        }
        int right = 0;
        if (j+1 < matrix[0].length && matrix[i][j+1] == matrix[i][j]) {
            right = dfs(matrix, i, j+1);
        }
        int left = 0;
        if (j-1 >= 0 && matrix[i][j-1] == matrix[i][j]) {
            left = dfs(matrix, i, j-1);
        }
        visited[i][j] = false;
        return 1 + Math.max(up, Math.max(down, Math.max(left, right)));
    }

    public static void main(String[] args) {
        int[][] mat = {
                       {9, 9, 9, 9, 9, 9, 9},
                       {9, 9, 8, 9, 9, 9, 9},
                       {9, 9, 9, 12, 9, 9, 9},
                       {9, 9, 9, 12, 9, 9, 9},
                       {9, 9, 9, 12, 9, 9, 9},
                       {9, 9, 9, 12, 9, 9, 9}
                      };
        System.out.println(longestPath(mat));
    }
}

'''
class Solution:
  ## not like maxArea, we need backtrack this question to avoid unlimit loop
  # 这个题和maxarea的区别就是因为不同value 不可以被染色。 所以要用backtrack的方式来做
    def maxArea(self,grid:list[list[int]]):
        if not grid: return 0
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        def dfs(row,col):
            if visited[row][col]:
              return 0

            visited[row][col] = True

            left = 0
            if 0<= row-1 < rows and grid[row - 1][col] == grid[row][col]:
                left = dfs(row - 1 , col)
            right = 0
            if 0<= row + 1 < rows and grid[row + 1][col] == grid[row][col]:
                right = dfs(row + 1 , col)
            up = 0
            if 0<= col - 1 < cols and grid[row ][col - 1] == grid[row][col]:
                up = dfs(row , col - 1)
            down = 0
            if 0 <= col + 1 < cols and grid[row][col + 1] == grid[row][col]:
              down = dfs(row, col + 1)

            visited[row][col] = False
            return 1 + max(up,max(down,max(left,right)))

        for i in range(rows):
            for j in range(cols):
                res = max(res,dfs(i,j))

        return res


nums = [[7,5,6,6,6,6],[7,7,4,6,6,6],[7,7,1,2,3,6],[7,1,7,7,3,2],[7,7,7,7,7,1],[1,1,1,1,1,1]]
sol = Solution()
print(sol.maxArea(nums))

