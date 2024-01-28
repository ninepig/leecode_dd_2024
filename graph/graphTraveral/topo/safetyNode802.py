'''
这个题是topo的应用题
1 最终安全节点是出度为0
2 为了找出安全节点，可以采取逆序建图的方式，将所有边进行反向。这样出度为
 的终点就变为了入度为 0 的点
3 安全节点如果没有环 那他的入度是0 (经过topo排序), 因为有环入度就不能为0
4 所以topo排序 找最终入度(排除环)以后的节点
'''
import collections


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
         #build reverse graph
        graph_dict = dict()
        for i in range (len(graph)):
            graph[i] = []
        for u in graph:
            for v in graph[u]:
                graph_dict[v].append(u) # build reverse graph , v is target but after reverse it is start

        # get indegree
        indegree = {u:0 for u in graph_dict}
        for u in graph_dict:
            for v in graph_dict[u]:
                indegree[v] += 1

        queue = collections.deque([u for u in graph if u == 0])

        while queue:
            cur = queue.popleft()
            for v in graph_dict[cur]:
                indegree[v] -=1
                if indegree[v] == 0:
                    queue.append(v)

        res = []
        for u in indegree:
            if u == 0:
                res.append(u)

        return res
