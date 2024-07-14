'''
1 塔普排序 先找环是否存在
2 如果环存在 查找环长度
复杂 但是不难
感觉不会问 ng个人出题

'''
class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        n = len(edges)

        # 记录节点入度
        indeg = [0] * n
        for u in edges:
            if u == -1:
                continue
            indeg[u] += 1

        # 拓扑排序【得到有向环中的全部节点】
        queue = [u for u in range(n) if indeg[u] == 0]
        while queue:
            u = queue.pop()
            v = edges[u]  # 节点u指向节点v：u -> v
            if v == -1:
                continue
            indeg[v] -= 1
            if indeg[v] == 0:  # 入度为 0 的节点入队列
                queue.append(v)

        # 无环，直接返回-1
        if max(indeg) == 0:
            return -1

        # BFS计算环的大小
        def bfs(u):
            step = 0
            while True:
                if u in visited:  # 完成闭环，返回环的长度
                    return step
                visited.add(u)
                u = edges[u]  # 环中的下一个节点
                step += 1

        # 遍历有向环中的所有节点
        ans = 0  # 最长环
        visited = set()  # 防止重复访问
        for u in range(n):
            if indeg[u] == 0 or u in visited:  # 每个节点至多存在于一个环中，且若已访问过则无需再次访问
                continue
            circle_len = bfs(u)
            ans = max(ans, circle_len)  # 尝试更新最长环

        return ans


# 作者：flix
# 链接：https: // leetcode.cn / problems / longest - cycle - in -a - graph / solutions / 1710861 / by - flix - gcit /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。