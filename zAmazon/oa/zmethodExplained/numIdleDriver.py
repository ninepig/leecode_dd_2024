#https://www.fastprep.io/problems/amazon-num-idle-drives
'''

Amazon uses small, Roomba-shaped robots, called "Drives".
They deliver large stacks of products to human workers by following set paths around the warehouse.

The warehouse can be represented in the form of a cartesian plane,
 where robots are located at integral points of the form (x, y).
 When a product is to be delivered to some point (i, j), the nearest robot is sought and chosen.
  Thus if a robot is surrounded by other robots nearby, it will seldom be chosen for work. More formally, a robot is said to be idle if it has a robot located above, below, left, and right of it. It is guaranteed that no two robots are at the same location.

Given the locations of n robots, find the number of idle robots.

'''
from typing import List


##建一个 x y轴的map （list）
## 看这个map上是否有点
## 如果没有点 就说明不是idle的
class Solution:
  def numIdleDrives(self, x: List[int], y: List[int]) -> int:
      hash_set = set()
      assert len(x) == len(y)
      col_ranges = {}
      row_ranges = {}
      for x_c, y_c in zip(x, y):
          if x_c in col_ranges:
              col_ranges[x_c].append(y_c)
              col_ranges[x_c].sort()
          else:
              col_ranges[x_c] = [y_c]
          if y_c in row_ranges:
              row_ranges[y_c].append(x_c)
              row_ranges[y_c].sort()
          else:
              row_ranges[y_c] = [x_c]

      active_cnt = 0
      for x_c, y_c in zip(x, y):
          is_active = False
          if x_c == row_ranges[y_c][0] or x_c == row_ranges[y_c][-1]:
              is_active = True
          if y_c == col_ranges[x_c][0] or y_c == col_ranges[x_c][-1]:
              is_active = True
          if is_active:
              active_cnt += 1
      return len(x) - active_cnt


sol = Solution()
x_list = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
y_list = [1, 2, 3, 1, 2, 3, 5, 1, 2, 3]
print(sol.numIdleDrives(x_list,y_list))