class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        size = len(nums)
        def dfs(pos,cur_sum):
            if pos == size:
                if cur_sum == target:
                    return 1
                else:
                    return 0
            # 标准的最简单dfs, dfs层,计数,增加pos数量
            ans = dfs(pos + 1 , cur_sum - nums[pos]) + dfs(pos + 1 , cur_sum + nums[pos])
            return ans
        return dfs(0,0)

    class Solution:
        def findTargetSumWaysMem(self, nums: List[int], target: int) -> int:
            size = len(nums)
            table = dict()

            def dfs(i, cur_sum):
                if i == size:
                    if cur_sum == target:
                        return 1
                    else:
                        return 0
                # 记忆化的过程. 把当前层处理的dfs 放到memory之中,避免重复
                if (i, cur_sum) in table:
                    return table[(i, cur_sum)]

                cnt = dfs(i + 1, cur_sum - nums[i]) + dfs(i + 1, cur_sum + nums[i])
                table[(i, cur_sum)] = cnt
                return cnt

            return dfs(0, 0)