# 作者：lucifer
# 链接：https://leetcode.cn/problems/possible-bipartition/solutions/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def dfs(self, graph, colors, i, color, N):
        colors[i] = color
        for j in range(N):
            # dislike eachother
            if graph[i][j] == 1:
                if colors[j] == color:
                    return False
                if colors[j] == 0 and not self.dfs(graph, colors, j, -1 * color, N):
                    return False
        return True

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[0] * N for i in range(N)]
        colors = [0] * N
        for a, b in dislikes:
            graph[a - 1][b - 1] = 1
            graph[b - 1][a - 1] = 1
        for i in range(N):
            if colors[i] == 0 and not self.dfs(graph, colors, i, 1, N):
                return False
        return True


