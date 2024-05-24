import collections

'''
从每个表示门开始，使用广度优先搜索去照门。因为广度优先搜索保证我们在搜索 dist + 1 距离的位置时，距离为 dist 的位置都已经搜索过了。所以每到达一个房间的时候一定是最短距离。
'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        inf = 999
        length = len(rooms)
        width = len(rooms[0])
        queue = collections.deque([])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        # 从每一个门出发，找到房间，更新房间距离 ,(i,j,dist)
        for i in  range(length):
            for j in range(width):
                if rooms[i][j] == 0:
                    queue.append((i,j,0))

        while queue:
            cur = queue.popleft()
            for direction in directions:
                new_x = cur[0]+direction[0]
                new_y = cur[1] + direction[1]
                if 0 <= new_x < length and 0<=new_y < width and rooms[new_x][new_y] == inf:
                    rooms[new_x][new_y] = direction[2] + 1 #设置到门的距离
                    queue.append((new_x,new_y,rooms[new_x][new_y])) #因为不是墙 所以可以继续入队
        
