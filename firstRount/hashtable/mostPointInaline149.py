'''
经典的数学题+ hashmap
slope的概念--》斜度
两个点可以确定一条直线，固定其中一个点，求其他点与该点的斜率，斜率相同的点则在同一条直线上。可以考虑把斜率当做哈希表的键值，存储经过该点，不同斜率的直线上经过的点数目。

对于点 i，查找经过该点的直线只需要考虑 (i+1,n-1) 位置上的点即可，因为 i-1 之前的点已经在遍历点 i-2 的时候考虑过了。
因为斜率是小数会有精度误差，所以我们考虑使用 (dx, dy) 的元组作为哈希表的 key。


这题不难 关键是各种case要熟悉

'''
import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3 : return n
        ans = 0
        for i in range(n):
            line_dict = dict()
            line_dict[0] = 0
            same = 1
            for j in range(i + 1 , n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[j][1]
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                gcd_dx_dy = math.gcd(abs(dx),abs(dy))
                if (dx > 0 and dy > 0) or (dx < 0 and dy < 0):
                    dx = dx / gcd_dx_dy
                    dy = dy / gcd_dx_dy
                elif dx < 0 and dy > 0:
                    dx = - dx/ gcd_dx_dy
                    dy = dy / gcd_dx_dy
                elif dx > 0 and dy < 0:
                    dx = dx / gcd_dx_dy
                    dy = - dy/ gcd_dx_dy
                elif dx == 0 and dy != 0:
                    dy = 1
                elif dx != 0 and dy == 0:
                    dx = 1
                key = (dx, dy)
                if key in line_dict:
                    line_dict[key] += 1
                else:
                    line_dict[key] = 1
            ans = max(ans, same + max(line_dict.values()))

        return ans

