class Solution:
    '''
    空间复杂度是 1 所以不能用set map 其他数组
    时间复杂度 n2以下 所以可以二分法
    利用二分查找的思想。用两个指针 left，right。left 指向 1，right 指向 n。将区间 [1, n] 分为 [left, mid] 和 [mid + 1, right] 。
    对于中间数 mid，统计 nums 中小于等于 mid 的数个数 cnt。
    如果 cnt 小于等于 mid，则重复数一定不会出现在左侧区间，那么从右侧区间开始搜索。若 cut 大于 mid，则重复数出现在左侧区间，则从左侧区间开始搜索。
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1

            if cnt <= mid:
                left = mid + 1
            else:
                right = mid

        return left