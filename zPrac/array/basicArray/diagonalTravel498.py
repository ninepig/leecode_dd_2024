'''
规律题
如果数值（行+列）是偶数 往右上方移动
如果数值是奇数 往左下方移动
边界条件
上行：
第一行 ， 往右移动 y+1
最后一列 向下移动 x+1
正常 x-1 y+=1
下行
第一列，往下移动 x+=1
最后一行 往右移动 y+ 1
正常 x+1 y-=1
'''
#o(n) time o (n) space
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        count = rows * cols
        x, y = 0, 0
        ans = []

        for i in range(count):
            ans.append(mat[x][y])
            if (x+y) % 2 == 0:
              # 四个角的问题
              #必须先判断到corner的case， 所以需要先判断是否到最右侧，先往下移动才安全
               if y == cols -1 :
                   x += 1
               elif x == 0:
                   y += 1
               else:
                   x -= 1
                   y += 1
            else:
                # 必须先判断到corner的case， 所以需要先判断是否到最下面，先往右侧移动才安全
                if x == rows -1:
                    y += 1
                elif y == 0:
                    x += 1
                else:
                    x += 1
                    y -= 1

        return ans