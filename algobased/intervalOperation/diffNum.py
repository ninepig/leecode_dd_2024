class diffNum:
    def __init__(self, nums : list[int]):

        self.diff = [0 for _ in range(len(nums))]
        self.diff[0] = nums[0]
        for i in range(1,len(nums)):
            self.diff[i] = nums[i] - nums[i-1]

    # increase start val  means increase val from i to end
    # decrease end + 1 val means decrease val from j + 1 to end of array
    def increment(self, start, end,val):
        self.diff[start] += val
        if end + 1 < len(self.diff):
            self.diff[end + 1 ] -= val

    # 把diff得数加回来
    def result(self):
        res = [0 for _ in range(self.diff)]
        res[0] = self.diff[0]
        for i in range(1,len(self.diff)):
            res[i] = res[i-1] + self.diff[i]

        return res