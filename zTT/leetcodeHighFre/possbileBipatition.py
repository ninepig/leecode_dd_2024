class Solution:
    ## 二分 染色法来做。 先构图，再对每个点进行染色法。
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # build adjacency list
        adjDic = {i: [] for i in range(n)}
        for u, v in dislikes:
            adjDic[u - 1].append(v - 1)
            adjDic[v - 1].append(u - 1)

        # color nodes
        visited = [0] * n

        for i in range(n):
            if visited[i] == 0:
                Q = deque()
                visited[i] = 1
                Q.append(i)

                while Q:
                    cur = Q.popleft()
                    for j in adjDic[cur]:
                        if visited[j] == 0:
                            visited[j] = -visited[cur]
                            Q.append(j)
                        elif visited[j] == visited[cur]:
                            return False

        return True
