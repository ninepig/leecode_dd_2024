import collections


class Solution:
    def dfs_recursiveBasic(self, graph, u, visited):
        print(u)  # 访问节点
        visited.add(u)  # 节点 u 标记其已访问

        for v in graph[u]:
            if v not in visited:  # 节点 v 未访问过
                # 深度优先搜索遍历节点
                self.dfs_recursive(graph, v, visited)

    def dfs_recursiveTwice(self, graph, u, visited):
        if visited[u]!=2:
            print(u)  # 访问节点
            visited[u] += 1  # 节点 u 标记其已访问

        for v in graph[u]:
            if v not in visited or visited[u] != 2:  # 节点 v 未访问过
                # 深度优先搜索遍历节点
                self.dfs_recursiveTwice(graph, v, visited)


graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D", "G"],
    "G": []
}

# 必须访问两次
visited = collections.defaultdict(int)
Solution().dfs_recursiveTwice(graph, "A", visited)
