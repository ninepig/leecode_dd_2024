'''
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.
'''
class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        ans = -1
        for i in range(len(edges)):
            curr = i
            path = []
            while edges[curr] >= 0:  # follow path until end or visited node
                path.append(curr)
                next = edges[curr]
                edges[curr] = -1   # mark as visited
                curr = next
            if curr in path:  # cycle found
                ans = max(ans, len(path)-path.index(curr)) # cycle length is path length minus nodes not in cycle
        return ans