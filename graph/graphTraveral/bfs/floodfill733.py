import collections

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 加visit 也可以处理
        if newColor == image[sr][sc]:
            return image
        queue = collections.deque([])
        # visit = set()
        queue.append((sr,sc))
        # visit.add((sr,sc))
        m = len(image)
        n = len(image[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ori_color = image[sr][sc]
        while queue:
            cur_pos = queue.popleft()
            ## 这个要放在popleft的时候加，因为第一个点需要被染色。。对于每一层的逻辑 bfs一定要在当前层pop时候处理，在别的地方处理会miss
            ## 或者第一个节点我们已经在while 之外处理过 就可以。
            image[cur_pos[0]][cur_pos[1]] = newColor
            for direction in directions:
                new_x = cur_pos[0] + direction[0]
                new_y = cur_pos[1] + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n  and image[new_x][new_y] == ori_color:
                    # visit.add((new_x,new_y))
                    ##放这里逻辑就错了
                    ##image[new_x][new_y] = newColor
                    queue.append((new_x,new_y))

        return  image