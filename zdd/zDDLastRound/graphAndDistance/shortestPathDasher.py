import collections

'''
https://leetcode.com/discuss/interview-question/1353434/Doordash-Phone-Screen-or-Senior-Software-Engineer-or-July-2021
A dasher sometimes travels between cities. To avoid delays, the dasher first checks for the shortest routes.
 Given a map of the cities and their bidirectional roads represented by a graph of nodes and edges, 
 determine which given roads are along any shortest path. Return an array of strings, one for each road in order,
  where the value is YES if the road is along a shortest path or NO if it is not.The roads or edges are named using their 1-based index within the input arrays.

Example
given a map of g_nodes = 5 nodes, the starting nodes, ending nodes and road lengths are:

Road from/to/weight
1 (1, 2, 1)
2 (2, 3, 1)
3 (3, 4, 1)
4 (4, 5, 1)
5 (5, 1, 3)
6 (1, 3, 2)
7 (5, 3, 1)

Example Input: (5, [1, 2, 3, 4, 5, 1, 5], [
2, 3, 4, 5, 1, 3, 3], [1, 1, 1, 1, 3, 2, 1])
The traveller must travel from city 1 to city g_nodes, so from node 1 to node 5 in this case.
The shortest path is 3 units long and there are three paths of that length: 1 → 5, 1 → 2 → 3 → 5, and 1 → 3 → 5.
Return an array of strings, one for each road in order, where the value is YES if a road is along a shortest path or NO if it is not. 
In this case, the resulting array is ['YES', 'YES', 'NO', 'NO', 'YES', 'YES', 'YES'].
 The third and fourth roads connect nodes (3, 4) and (4, 5) respectively. They are not on a shortest path, i.e. one with a length of 3 in this case.

'''

'''
1 构图
2 bfs 找所有达到目标点
3 然后不断更新最短路径

'''


def find_shortest_paths_2(node_g, src, dest, weight):
    graph = collections.defaultdict(list)
    for i in range(len(src)):
        s, d = src[i], dest[i]
        graph[s].append(i)
        graph[d].append(i)

    print("graph",graph)

    ## queue  (city, cur_distance, visited)
    q = [(1, 0, set())]
    min_distance = float('inf')
    all_min_path = []

    while (q):
        city, dist, visited = q.pop()
        print(city, visited, dist)
        if city == node_g:
            if dist < min_distance:
                min_distance = dist
                all_min_path = []
            all_min_path.append(list(visited))

        if dist < min_distance:
            for edge_idx in graph[city]:
                if edge_idx not in visited:
                    if dest[edge_idx] == city:
                        ## set union can be performed with the | operator:
                        q.append((src[edge_idx], dist + weight[edge_idx], visited | {edge_idx}))
                    else:
                        q.append((dest[edge_idx], dist + weight[edge_idx], visited | {edge_idx}))

    ans = ['NO'] * len(dest)
    for min_path in all_min_path:
        for edge_idx in min_path:
            ans[edge_idx] = 'YES'
    return ans


if __name__ == '__main__':
    ans = find_shortest_paths_2(
        5,
        [1, 2, 3, 4, 5, 1, 5],
        [2, 3, 4, 5, 1, 3, 3],
        [1, 1, 1, 1, 3, 2, 1]
    )
    print(ans)
