'''
这个题就是个dfs + mem
如果要输出 就是回溯法
那就比较难了
'''
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        size = len(nums)
        def dfs(pos,cur_target):
            if pos == size:
                if cur_target == target:
                    return 1
                else:
                    return 0
            ans =  dfs(pos + 1 , cur_target + nums[pos]) + dfs(pos + 1, cur_target - nums[pos])
            return ans

        return dfs(0,0)


    # Dfs + memo
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        size = len(nums)
        memo = dict()
        def dfs(pos,cur_target):
            ## 结局问题的核心 dfs的核心
            if pos == size:
                if cur_target == target:
                    return 1
                else:
                    return 0
            if (pos, cur_target) in memo:
                return memo[(pos,cur_target)]
            ans =  dfs(pos + 1 , cur_target + nums[pos]) + dfs(pos + 1, cur_target - nums[pos])
            memo[(pos,cur_target)] = ans
            return ans

        return dfs(0,0)