'''
你是一个开公交车的司机，公交车的最大载客量为 capacity，沿途要经过若干车站，给你一份乘客行程表 int[][] trips，
其中 trips[i] = [num, start, end] 代表着有 num 个旅客要从站点 start 上车，到站点 end 下车，请你计算是否能够一次把所有旅客运送完毕（不能超过最大载客量 capacity）。
'''

class diff
    def __init__(self,nums):
        self.diff =[ 0 for _ in range(len(nums))]
        self.diff[0] = nums[0]
        for i in range(1,len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    def increment(self,i , j , val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self):
        res = [0 for _ in range(len(self.diff))]
        res[0] = self.diff[0]
        for i in range(1,len(self.diff)):
            res[i] = res[i-1] + self.diff[i]

        return res

class solution:
    def carPooling(trips: List[List[int]], capacity: int) -> bool:
        nums = [0] * 1001
        diffTool = diff(nums)
        for trip in trips:
            i = trip[1]
            j = trip[2] - 1 # 下车的话 j的位置就要减去乘客
            val = trip[0]
            diffTool.increment(i,j,val)
        res = diffTool.result()
        for i in range(len(res)):
            if res[i] > capacity:
                return False
        return True