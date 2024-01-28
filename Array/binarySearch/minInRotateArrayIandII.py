class Solution:
    '''
    这两个题关键还是画图 一定要画图明白原理。 画完就清晰了




    创建两个指针 left、right，分别指向数组首尾。让后计算出两个指针中间值 mid。将 mid 与两个指针做比较。

如果 nums[mid] > nums[right]，则最小值不可能在 mid 左侧，一定在 mid 右侧，则将 left 移动到 mid + 1 位置，继续查找右侧区间。
如果 nums[mid] ≤ nums[right]，则最小值一定在 mid 左侧，或者 mid 位置，将 right 移动到 mid 位置上，继续查找左侧区间。
    '''
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


'''
创建两个指针 left、right，分别指向数组首尾。让后计算出两个指针中间值 mid。将 mid 与右边界进行比较。

如果 nums[mid] > nums[right]，则最小值不可能在 mid 左侧，一定在 mid 右侧，则将 left 移动到 mid + 1 位置，继续查找右侧区间。
如果 nums[mid] < nums[right]，则最小值一定在 mid 左侧，将 right 移动到 mid 位置上，继续查找左侧区间。
当 nums[mid] == nums[right]，无法判断在 mid 的哪一侧，可以采用 right = right - 1 逐步缩小区域。
'''
        def findMinII(self, nums: List[int]) -> int:
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                elif nums[mid] < nums[right]:
                    right = mid
                else:
                    right = right - 1
            return nums[left]