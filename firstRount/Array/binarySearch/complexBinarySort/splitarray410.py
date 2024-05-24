'''
可以用二分查找来找这个子数组和的最大值，我们用 ans 来表示这个值。ans 最小为数组 nums 所有元素的最大值，最大为数组 nums 所有元素的和。即 ans 范围是 [max(nums), sum(nums)]。

所以就确定了二分查找的两个指针位置。left 指向 max(nums)，right 指向 sum(nums)。然后取中间值 mid，计算当子数组和的最大值为 mid 时，所需要分割的子数组最少个数。

如果需要分割的子数组最少个数大于 m 个，则说明子数组和的最大值取小了，不满足条件，应该继续调大，将 left 右移，从右区间继续查找。
如果需要分割的子数组最少个数小于或等于 m 个，则说明子数组和的最大值满足条件，并且还可以继续调小，将 right 左移，从左区间继续查找，看是否有更小的数组和满足条件。
最终，返回符合条件的最小值即可。
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def get_count(x):
            total = 0
            count = 1
            for num in nums:
                if total + num > x:
                    count += 1
                    total = num
                else:
                    total += num
            return count

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if get_count(mid) > m:
                left = mid + 1
            else:
                right = mid
        return left