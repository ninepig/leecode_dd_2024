from typing import List


class Solution:
    ## 这个题的关键 就是所谓的对角线 用的是 i +j 作为标准 如果 i+j 是even的 那就是往上走 ，然后利用一个dict来做 非常优雅
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or len(mat) == 0 :
            return []
        res = []
        dict = {}
        row = len(mat)
        col = len(mat[0])
        for i in range(row):
            for j in range(col):
                if (i + j) in dict:
                    dict[i+j].append(mat[i][j])
                else:
                    dict[i+j] = [mat[i][j]] ## 为空的话 就需要一个新建list

        for key in dict:
            ## 余数不为零的情况 那就是正向的 不需要reverse
            if key % 2 != 0:
                res.extend(dict[key])
            else:
                res.extend(dict[key][::-1])

        return res