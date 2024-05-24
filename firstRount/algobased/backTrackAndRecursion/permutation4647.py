from firstRount.LinkedList import List


class Solution:
    # 回溯法
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        path = []
        def backtrack(nums):
            if len(path) == len(nums):
                res.append(path[:])
                return  ## 一定要有结束条件

            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(nums)
                    path.pop()
        backtrack(nums)
        return res

    def permuteAnswer(self, nums: List[int]) -> List[List[int]]:
        res = []  # 存放所有符合条件结果的集合
        path = []  # 存放当前符合条件的结果

        def backtracking(nums):  # nums 为选择元素列表
            if len(path) == len(nums):  # 说明找到了一组符合条件的结果
                res.append(path[:])  # 将当前符合条件的结果放入集合中
                return

            for i in range(len(nums)):  # 枚举可选元素列表
                if nums[i] not in path:  # 从当前路径中没有出现的数字中选择
                    path.append(nums[i])  # 选择元素
                    backtracking(nums)  # 递归搜索
                    path.pop()  # 撤销选择

        backtracking(nums)
        return res

    def permuteUniqueMy(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        nums.sort() # 很重要
        visit = [False for _ in range(len(nums))]
        def backtrack(nums):
            ## ending
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                # 去重的过程
                if i > 0 and nums[i] == nums[i - 1] and not visit[i-1]:
                    continue

                if not visit[i]:
                    visit[i] = True
                    path.append(nums[i])
                    backtrack(nums)
                    path.pop()
                    visit[i] = False

        backtrack(nums)
        return res


class Solution2:
    res = []
    path = []
    def backtrack(self, nums: List[int], visited: List[bool]):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            if not visited[i]:
                visited[i] = True
                self.path.append(nums[i])
                self.backtrack(nums, visited)
                self.path.pop()
                visited[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res.clear()
        self.path.clear()
        nums.sort()
        visited = [False for _ in range(len(nums))]
        self.backtrack(nums, visited)
        return self.res