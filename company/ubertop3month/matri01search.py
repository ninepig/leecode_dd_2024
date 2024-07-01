### https://www.1point3acres.com/bbs/thread-1071664-1-1.html
import bisect


class solution:
    ## binary search  nlogn
    def searchFirstOneInMatrics(self, matrix:list[list[int]]):
        ## giving u a matrix with 01 only, when 1 show up, no way to get 0 any more
        ## get first 1's column number
        m = len(matrix)
        n = len(matrix[0])
        ## need ask if we need smallest column or first column
        target = 0
        for i in range(m):
            for j in range(n):
                pos = bisect.bisect_left(matrix[i],1)
                ## if that is first , we break here
                target = min(pos,target)

        return target

    def searchFirstOneInMatricsMN(self, matrix:list[list[int]]):
        m = len(matrix)
        n = len(matrix[0])
        ## need ask if we need smallest column or first column
        target = 0
        for i in range(0,m+n):
            if i < m and i < n:
                ## we try to find 1 in diagnal line
                if matrix[i][i] == 1 :
                    target = i
                    break
        ## after we find first row , we try to search for first 1 in that row

        col_target = 0
        for i in range(n):
            if matrix[target][i] == 1 :
                col_target = i
                break

        return col_target


# test = [0,0,1,1,1]
# pos = bisect.bisect_left(test,1)
# print(pos)

