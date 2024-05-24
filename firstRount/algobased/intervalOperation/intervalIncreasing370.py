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
    '''
    假设你有一个长度为 n 的数组，初始情况下所有的数字均为 0，你将会被给出 k​​​​​​​ 个更新的操作。

    其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，你需要将子数组 A[startIndex ... endIndex]（包括 startIndex 和 endIndex）增加 inc。
    '''
    def getModifiedArray(length: int, updates: List[List[int]]) -> List[int]:
        num = [0] * length
        diffHelper = diff(num)
        for update in updates:
            i,j,val = update[0],update[1],update[2]
            diffHelper.increment(i,j,val)

        return diffHelper.result()
    
