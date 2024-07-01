from collections import Counter


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = left = 0
        cnt = Counter()
        for right, x in enumerate(nums):
            cnt[x] += 1
            while cnt[x] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/solutions/2560708/hua-dong-chuang-kou-fu-ti-dan-pythonjava-6fxo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。