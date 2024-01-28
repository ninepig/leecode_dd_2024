class fenwayTree:
    def __init__(self,nums):
        self.nums = nums
        # +1 是关键点 , fenwaytree多一位
        self.fenwayTree = [0 for _ in range(len(nums) + 1)]
        ## initial process
        for i , val in enumerate(nums):
            self.update(i, val)

    def __lowbit(self,index):
        return index & (-index)

    def update(self, i, val):
        while i < len(self.fenwayTree):
            self.fenwayTree[i] += val
            i += self.__lowbit(i)


    def query(self,index):
        res = 0
        while index:
            res += self.fenwayTree[index]
            index -= self.__lowbit(index)




