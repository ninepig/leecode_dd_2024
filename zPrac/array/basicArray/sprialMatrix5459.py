class Solution:
    '''
    用四个flag来模拟移动
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        left , right , up, down = 0, cols - 1 ,0 , rows -1
        while True:
            #从左到右
            for i in range(left,right + 1):
                res.append(matrix[up][i])
            up += 1
            if up > down:
                break
            # from top to down
            for i in range(up,down + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            # from right to left
            for i in range(right,left - 1 , -1):
                res.append(matrix[down][i])
            down -= 1
            if down > up:
                break
            # from bottom to top
            for i in range(down,up - 1 , -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return res

    class Solution:
        def generateMatrix(self, n: int) -> List[List[int]]:
            if n <= 0 :
                return []
            res = [[0 for i in range(n)] for i in range(n)]
            index = 1
            left , right , top , bottom = 0, n-1 , 0 , n-1
            while True:
                for i in range(left,right + 1):
                    res[top][i] = index
                    index += 1
                top += 1
                if top > bottom:
                    break

                for i in range(top,bottom + 1):
                    res[i][right] = index
                    index += 1
                right -= 1
                if right < left :
                    break

                for i in range(right , left - 1, -1):
                    res[bottom][i] = index
                    index += 1
                bottom -=1

                if bottom < top:
                    break

                for i in range(bottom,top -1 , -1):
                    res[i][left] = index
                    index +=1
                left += 1
                if left > right:
                    break

            return res
