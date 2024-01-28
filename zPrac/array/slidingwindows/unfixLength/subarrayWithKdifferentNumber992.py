class Solution:
    '''这个题很特别, 因为要恰好等于k个不同的数
    所以转换成
    恰好包含 k 个不同整数的连续子数组数量 = 包含小于等于 k 个不同整数的连续子数组数量 - 包含小于等于 k - 1 个不同整数的连续子数组数量'''
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        return self.subArrayWithAtLeastDist(nums,k) - self.subArrayWithAtLeastDist(nums,k-1)

    ## 关键是
    def subArrayWithAtLeastDist(self, nums, k):
        windows = dict()
        left , right = 0, 0
        ans = 0
        while right < len(nums):
            if nums[right] not in windows:
                windows[nums[right]] = 1
            else:
                windows[nums[right]] += 1

            while len(windows) > k:
                if nums[left] in windows:
                    windows[nums[left]] -= 1
                if windows[nums[left]] == 0:
                    del  windows[nums[left]]
                left += 1

            ans += right - left + 1 # subarray number , we can accumulate all of them

            right += 1

        return ans