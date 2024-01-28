'''
dp的背包问题
但是这里用bfs来做
'''
import collections
import math


class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0 : return 0
        queue = collections.deque([])
        visited = set()
        visited.add(n)
        queue.append(n)
        count = 0

        while queue:
            count += 1
            for _ in range(len(queue)):
                value = queue.pop()
                print("value",value)
                ## 利用当前value  (i , int(math.sqrt(value)) + 1) 来作为当前层有可能出现的所有step 可能性
                for i in range(1 , int(math.sqrt(value)) + 1):
                    x = value - i * i
                    print("x", x)
                    if x == 0:
                        return count
                    if x not in visited:
                        visited.add(x)
                        queue.appendleft(x)


so = Solution()
print(so.numSquares(27))

'''
   value 25
   x 24
   x 21
   x 16
   x 9
   x 0
   1
   一个循环全部走完。 所以只需要一层
   '''