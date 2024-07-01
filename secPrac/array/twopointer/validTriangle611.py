'''
e1 + e2 > e3 ( triangle policy)
'''

class Solution:
    ## 对撞指针 sort是第一步
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(2,len(nums)):
            left = 0
            right = i - 1 # fix one edge on rightest side
            while left < right:
                if nums[left] + nums[right] <= nums[i]: # 不满足条件, 左侧加1
                    left += 1
                else:
                    ans += (right - left) # 满足条件的话 right - left之间所有的值都满足
                    right -= 1

        return  ans
    