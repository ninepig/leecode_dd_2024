class Solution:
    '''o(n) +_ logn'''
    def searchMatrixIsolution1(self, matrix: List[List[int]], target: int) -> bool:
        list1=[]
        for row in matrix:
            if row[-1]>=target:
                list1=row
                break
        left,right=0,len(list1)-1
        while left<=right:
            mid=(right+left)//2
            if list1[mid]==target:
                return True
            elif list1[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False

    def searchMatrixPureBinary(self, matrix: List[List[int]], target: int) ->
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1
        while left <= right:
            mid = left + (right - left) // 2
            num = matrix[mid // col][mid % col]
            if num == target:
                return True
            if num > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    '''https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/2324351/python-explained/
    对于这样的二维矩阵 要观察。 左下角是初始点。 往上变小 往右变大。 这样就形成二分法得原则
    '''

    def searchMatrix2(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat)
        n = len(mat[0])

        i = m - 1
        j = 0

        while i >= 0 and j < n:
            if mat[i][j] == target:
                return True
            elif mat[i][j] < target:
                j += 1
            else:
                i -= 1

        return False
    '''
    或者先located 到某一行 
    '''
    def searchMatrix2seachfirst(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            if mat[i][0] <= target and mat[i][-1] >= target:
                lo = 0
                hi = n
                while (lo < hi):
                    mid = (lo + hi) // 2

                    if mat[i][mid] == target:
                        return True
                    elif mat[i][mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid

        return False