# https://leetcode.ca/2016-08-15-259-3Sum-Smaller/
## 双指针逼近。。sum系列
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s >= target:
                    k -= 1
                else:
                    ans += k - j
                    j += 1
        return ans