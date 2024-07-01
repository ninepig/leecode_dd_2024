#https://www.fastprep.io/problems/get-min-time
'''

Developers at Amazon have deployed an application with a distributed database. It is stored on total_servers different servers numbered from 1 to total_servers that are connected in a circular fashion, i.e. 1 is connected to 2, 2 is connected to 3, and so on until total_servers connects back to 1.

There is a subset of servers represented by an array servers of integers. They need to transfer the data to each other to be synchronized. Data transfer from one server to one it is directly connected to takes 1 unit of time. Starting from any server, find the minimum amount of time to transfer the data to all the other servers.

'''
from typing import List

## 正向 负向

class Solution:
  def getMinTime(self, total_servers: int, servers: List[int]) -> int:
      # Construct Index dict
      dict_servers = dict()
      for index in range(total_servers):
        dict_servers[index + 1] = index
      servers.sort()

      # Clockwise
      distance_clockwise = 0
      for i in range(len(servers) - 1):
        first, second = dict_servers[servers[i]], dict_servers[servers[i + 1]]
        distance_clockwise += second - first

      # ConterCLock
      distance_counter = 0
      servers.append(servers.pop(0))
      for i in range(len(servers) - 1, 0, -1):
        first, second = dict_servers[servers[i]], dict_servers[servers[i - 1]]
        if first - second < 0:
          distance_counter += first - second + total_servers
        else:
          distance_counter += first - second

      return min(distance_clockwise, distance_counter)

sol = Solution()
test = [4, 6, 2, 9]
total = 10
print(sol.getMinTime(total,test))