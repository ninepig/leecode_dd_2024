## https://leetcode.com/discuss/interview-experience/4718477/Uber-or-Phone-Screen-or-Amsterdam/
## https://www.1point3acres.com/bbs/thread-1071771-1-1.html

from collections import deque

'''
O(M*N*4*max(M, N))
面完后想了想，其实可以用 memo 优化，预先求出 2D array 中每个坐标点和 left, top, bottom, right 的 boundary/blocker 的距离，
之后对于每个 robot 直接 O(1) 查询距离就行。TC 可以到 O(M*N).
'''

def find_robots_with_matching_query(map, query):
    rows = len(map)
    cols = len(map[0]) if rows > 0 else 0

    # directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Top, bottom, left, right

    def distance_to_blocker_bfs(start_row, start_col, direction):
        queue = deque([(start_row, start_col, 0)])  # (current_row, current_col, distance)
        while queue:
            current_row, current_col, distance = queue.popleft()
            # Move in the specific direction
            next_row = current_row + direction[0]
            next_col = current_col + direction[1]
            # Check boundaries and blockers
            if not (0 <= next_row < rows and 0 <= next_col < cols) or map[next_row][next_col] == 'X':
                return distance + 1

            queue.append((next_row, next_col, distance + 1))

    # Find all robots
    robots = [(i, j) for i in range(rows) for j in range(cols) if map[i][j] == 'O']
    matching_robots = []

    # Check each robot if it matches the query
    for r, c in robots:
        distances = [
            distance_to_blocker_bfs(r, c, (0, -1)),  # Left
            distance_to_blocker_bfs(r, c, (-1, 0)),  # Top
            distance_to_blocker_bfs(r, c, (1, 0)),  # Bottom
            distance_to_blocker_bfs(r, c, (0, 1))  # Right
        ]

        if distances == query:
            matching_robots.append([r, c])

    return matching_robots