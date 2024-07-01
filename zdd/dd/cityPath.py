import collections


def find_shortest_paths_2(node_g, src, dest, weight):
    graph = collections.defaultdict(list)
    for i in range(len(src)):
        s, d = src[i], dest[i]
        graph[s].append(i)
        graph[d].append(i)

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