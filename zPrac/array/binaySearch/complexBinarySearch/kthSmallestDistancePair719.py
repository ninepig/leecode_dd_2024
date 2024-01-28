


class Solution:
    # k 小这种标题就是感觉用pq 来做, 这里用二分法来做 非常类似410的做法
    #找到一个 差值区间,不断二分法逼近, 毕竟的原则是pair数量大于k
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # 统计有多少个diff 数组 大于target ,利用要给滑动窗口
        def getDiffCount(mid):
            left = 0
            count = 0
            for right in range(1,len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += (right - left)
            return count

        nums.sort()
        left = 0
        right = nums[-1] - nums[0] # largest diff
        while left < right:
            mid = left + (right - left) // 2
            if getDiffCount(mid) > k:
                right = mid - 1
            else:
                left = mid

        return left
