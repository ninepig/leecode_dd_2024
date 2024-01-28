class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def backtrack(nums,index):
            res.append(path[:])
            if index >= len(nums):
                return

            # for i in range(nums): # 写错了 for i in range(index, len(nums)):
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(nums,i + 1) # 写错了
                path.pop()

        backtrack(nums,0)
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def backtrack(index):
            res.append(path[:])
            if index >= len(nums):
                return
            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i - 1] : # 重复出现，去重
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        nums.sort()
        backtrack(0)
        return res

class SolutionAnswer:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # 存放所有符合条件结果的集合
        path = []  # 存放当前符合条件的结果
        def backtracking(nums, index):          # 正在考虑可选元素列表中第 index 个元素
            res.append(path[:])                 # 将当前符合条件的结果放入集合中
            if index >= len(nums):              # 遇到终止条件（本题）
                return

            for i in range(index, len(nums)):   # 枚举可选元素列表
                path.append(nums[i])            # 选择元素
                backtracking(nums, i + 1)       # 递归搜索
                path.pop()                      # 撤销选择

        backtracking(nums, 0)
        return res

    def backtrack2(self, nums, index, res, path):
        res.append(path[:])

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.backtrack2(nums, i + 1, res, path)
            path.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, path = [], []
        self.backtrack2(nums, 0, res, path)
        return res