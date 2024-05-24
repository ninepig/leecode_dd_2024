class Solution:
    '''
    使用二维数组 board 来保存答案，初始情况下，board 中元素全部赋值为 0。
遍历二维数组的每一行，每一列。当前位置下的值为当前行的和与当前列的和的较小值，即 board[row][col] = min(rowSum[row], colSum[col])。
更新当前行的和，将当前行的和减去 board[row][col]。
更新当前列的和，将当前列的和减去 board[row][col]。
遍历完返回二维数组 board

wenjing
画图做
    '''
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        board = [[0 for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                board[i][j] = min(rowSum[i],colSum[j])
                rowSum[i] -= board[i][j]
                colSum[j] -= board[i][j]

        return board