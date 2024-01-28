class NumArray:

    def __init__(self, nums: List[int]):
        self.num = nums

    # 查询闭区间 [left, right] 的累加和
    # BF--> for loop doing this every time
    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for i in range(left,right + 1):
            res += self.num[i]

        return res

    def __init__(self, nums: List[int]):
        self.num = nums
        self.preSum = [0 for _ in range(len(nums) + 1)]
        for i in range(1,len(self.preSum)):
            self.preSum[i] = self.preSum[i - 1] + self.num[i-1]

    # 查询闭区间 [left, right] 的累加和
    # prefix Sum
    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]



class NumMatrix:
    def __init__(self, matrix:List[List[int]]):
        self.matrix = matrix
        self.preSum = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                self.preSum[i][j] = self.preSum[i-1][j] + self.preSum[i][j - 1] + self.matrix[i-1][j-1] - self.preSum[i - 1][j - 1]

    # x2, y2 is right bound , need + 1
    def sumRegion(self,x1,x2,y1,y2):
        return self.preSum[x2+1][y2+1] - self.preSum[x2+1][y1] - self.preSum[x1][y2 + 1] + self.preSum[x1][y1]