class NumArray:
    # https://leetcode.cn/problems/range-sum-query-mutable/solutions/1389182/qu-yu-he-jian-suo-shu-zu-ke-xiu-gai-by-l-76xj/
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.fenwayTree = [0 for _ in range(len(nums) + 1)]
        for i in range(nums):
            self.add(i,nums[i])

    def __lowbit(self,index):
        return index & (-index)

    ## fenway tree 更新的是delta
    def add(self,index,val):
        while index < len(self.fenwayTree):
            self.fenwayTree[index] += val
            index += self.__lowbit(index)

    def prefixSum(self,index):
        res = 0
        while index:
            res += self.fenwayTree[index]
            index -= self.__lowbit(index)
        return res

    ## 更新数组下标值 所以对应的fenway tree 是 更新 index+ 1 ，同时detla
    def update(self, index: int, val: int) -> None:
        self.add(index + 1 , val - self.nums[index])
        self.nums[index] = val


    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right + 1) - self.prefixSum(left)