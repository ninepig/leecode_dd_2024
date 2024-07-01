

# A DashMart is a warehouse run by DoorDash that houses items found in
# convenience stores, grocery stores, and restaurants. We have a city with open
# roads, blocked-off roads, and DashMarts.
#
# City planners want you to identify how far a location is from its closest
# DashMart.
#
# You can only travel over open roads (up, down, left, right).
#
# Locations are given in [row, col] format.
#
# Example:
#
# [
# # 0 1 2 3 4 5 6 7 8
# ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'], # 0
# ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'], # 1
# [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '], # 2
# [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '], # 3
# [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'], # 4
# [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X'] # 5
# ]
#
# ' ' represents an open road that you can travel over in any direction (up, down, left, or right).
# 'X' represents an blocked road that you cannot travel through.
# 'D' represents a DashMart.
## # list of pairs [row, col]
# locations = [
# [2, 2],
# [4, 0],
# [0, 4],
# [2, 6],
# ]
#
# answer = [1, 4, 1, 5]
#
# Implement Function:
# - get_closest_dashmart(city, locations)
#
# Provided:
# - city: List[str]
# - locations: List[List[int]]
#
# Return:
# - answer: List[int]


'''
1基本
  1.1 Input可能越界
2 followup
  1 已经标注
  比原题的变化是障碍格子虽然不能跃过，但是可以到达，因此也要计算距离，还有增加了一点 OO 的考察，写完之后有 follow-up，
  输入一些格子坐标，每个坐标关联到最近的门，返回每个门关联的坐标个数
  2 custmer 数量 需要考虑下
  找最近的dashmart。follow up是地图里除了有dashmart还有客户位置，每个客户由离得最近的dashmart服务（如果有多个超市到某个客户的距离都相同，则每个超市都能服务此客户）
  求服务客户数量最多的超市

'''

BLOCKED = "X"
OPEN = " "
DASH_MART = "D"

from collections import deque
def get_closest_dashmart(city, locations):
    queue = deque([])

    # Define surrounding directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Track the closes distances to a dash mart.
    distances = {}
    rows, cols = len(city), len(city[0])

    # Append all dash marts in the queue.
    for r in range(rows):
        for c in range(cols):
            if city[r][c] == DASH_MART:
                distances[(r, c)] = 0
                queue.append((r, c, 0))

    # Start BFS.
    while queue:
        curr_row, curr_col, dist = queue.popleft()

        # Check the cells around you.
        for x, y in directions:
            new_row, new_col = x + curr_row, y + curr_col

            # Check for boundaries
            # Check for cells that have not been "visited" before.
            # Check for open roads only.
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in distances and \
                    city[new_row][new_col] == OPEN:
                distances[(new_row, new_col)] = dist + 1
                queue.append((new_row, new_col, dist + 1))
            '''
            没什么悬念的 BFS，比原题的变化是障碍格子虽然不能跃过，但是可以到达，因此也要计算距离，还有增加了一点 OO 的考察，
            写完之后有 follow-up，输入一些格子坐标，每个坐标关联到最近的门，返回每个门关联的坐标个数
            如果是这个要求，那么x 就需要考虑了 如果是x 可以增加距离 但是不能加入queue之中
            '''

    # Loop over locations and get the distances.
    result = []
    for location in locations:
        result.append(distances[(location[0], location[1])])

    return result

city = [
    ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
    [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
    [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']
]

locations = [
    [2, 2],
    [4, 0],
    [0, 4],
    [2, 6],
]

print(get_closest_dashmart(city, locations))