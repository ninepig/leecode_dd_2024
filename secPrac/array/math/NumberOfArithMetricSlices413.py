class Solution:
    # 枚舉計數的等差數列做法
    # 暴力法优化
    # 从后往前
    # 没有面经可以不做 ， 数学推导很复杂。。
    # https://leetcode.cn/problems/arithmetic-slices/solutions/925973/deng-chai-shu-lie-hua-fen-by-leetcode-so-g7os

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        d, t = nums[0] - nums[1] , 0 # t means count
        ans = 0
        for i in range(2, n):
            if nums[i - 1] - nums[i] == d:
                t += 1
            else:
                d = nums[i - 1] - nums[i]
                t = 0
            ans += t

        return ans