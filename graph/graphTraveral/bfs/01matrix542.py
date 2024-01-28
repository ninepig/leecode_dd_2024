'''
思路 1：广度优先搜索
题目要求的是每个 1 到 0的最短曼哈顿距离。

比较暴力的做法是，从每个 1 开始进行广度优先搜索，每一步累积距离，当搜索到第一个 0，就是离这个 1 最近的 0，我们更新对应 1 位置上的答案距离。然后从下一个 1 开始进行广度优先搜索。

这样做每次进行广度优先搜索的时间复杂度为
。对于
 个节点来说，每个节点可能都要进行一次广度优先搜索，总的时间复杂度为
。时间复杂度太高了。

我们可以换个角度：求每个 0 到 1 的最短曼哈顿距离（和求每个 1 到 0 是等价的）。

我们将所有值为 0 的元素位置保存到队列中，然后对所有值为 0 的元素开始进行广度优先搜索，每搜一步距离加 1，当每次搜索到 1 时，
就可以得到 0 到这个 1 的最短距离，也就是当前离这个 1 最近的 0 的距离。

这样对于所有节点来说，总共需要进行一次广度优先搜索就可以了，时间复杂度为


wenjing: 把所有的0节点放入队列， 每次从他出发到达1的时候就是最近距离， 因为这是每一次bfs的过程。 是可以保证是最短距离。
。
'''

import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[0 for _ in range(m)] for _ in range(n)]
        queue = collections.deque([])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()
        # put 0 in to quque
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        # start from 0 , update level if not visited
        while queue:
            x,y = queue.popleft()
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < m and 0<= new_y < n and (new_x,new_y) not in visited:
                    visited.add((new_x,new_y))
                    res[new_x][new_y] = res[x][y] + 1
                    queue.append((new_x,new_y))

        return res