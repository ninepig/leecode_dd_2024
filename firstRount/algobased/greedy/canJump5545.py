class Solution:
    '''最基本的贪心
    只关注当前点能到达哪里'''
    def canJump(self, nums: List[int]) -> bool:
        if not nums :
            return False
        max_jump = 0
        for i in range(len(nums)):
            if max_jump >= i and i + nums[i] > max_jump:
                max_jump = i + nums[i]

        return max_jump > len(nums)

    '''非常巧妙的方法,只有index循环到最远位置的时候才计数,这个贪心..无敌.
    最优解'''
    def jump2(self, nums: List[int]) -> int:
        end, max_pos = 0, 0
        steps = 0
        for i in range(len(nums) - 1):
            max_pos = max(max_pos, nums[i] + i)
            if i == end:
                end = max_pos
                steps += 1
        return steps