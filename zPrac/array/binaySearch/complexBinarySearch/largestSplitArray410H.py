class Solution:
    '''这道题太难了...
    数学上 最小的和可以是数组最大值, m = 数组大小
    最大的值可以是m =1 , 数组和
    所以我们用二分法 找这个数 使得 可以分的子数组 = m
    '''
    def splitArray(self, nums: List[int], m: int) -> int:
        def get_count(x):
            total = 0
            count = 1
            # 如果total +num 大于 x 就说明我们有了一个子数组
            # 不大于x 可以需要下一个数构成subarray
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