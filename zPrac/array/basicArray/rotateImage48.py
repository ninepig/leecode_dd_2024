'''
有一个找规律题
顺时针90度
1 先水平翻转
2 主对角线翻转
'''

# 这个也是个常备题。 记住就行了
#o（n）

def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)

    #水平翻转
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j] ,matrix[n - i - 1][j] = matrix[n -i - 1][j],matrix[i][j]
    #主对角线翻转
    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]


