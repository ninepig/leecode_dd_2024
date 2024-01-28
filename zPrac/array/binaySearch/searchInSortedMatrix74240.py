class Solution:
    # 因为 matrix是sorted 所以可以看作是一个m*n的sorted array--》binary search 解决
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        size = rows*cols
        left = 0
        right = size - 1
        # not approching
        while left <= right:
            mid =  left + (right - left) // 2
            target_row,target_col = divmod(mid,cols) # find x,y
            if matrix[target_row][target_col] == target:
                return True
            elif matrix[target_row][cols] > target:
                right = mid
            else:
                left = mid
        return False

    # only row sorted, cols sorted, not sorted like an array
    # 从左角开始, 如果大于target 往上走, 小于target 往右走
    # o(m+n) 这个也适用于上一题
    def searchMatrixSecond(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row = rows - 1
        col = 0
        while row >= 0 and col < cols:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -=1
        return False

    # only row sorted, cols sorted, not sorted like an array
    def searchMatrixSecondBinarySearch(self, matrix: List[List[int]], target: int) -> bool:
        # binary search for each row
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            if matrix[i][0] <= target <= matrix[i][cols-1]:## start binary search
                left = 0
                right = cols - 1
                while  left <= right:
                    mid = left + (right - left) // 2
                    if matrix[mid] == target:
                        return True
                    elif matrix[mid] < target:
                        left = mid
                    else:
                        right = mid

        return False
