'''
乍一看是pq题
其实是二分+双指针
数组的区间为 [0, n-1]，查找的子区间长度为 k。我们可以通过查找子区间左端点位置，从而确定子区间。

查找子区间左端点可以通过二分查找来降低复杂度。

因为子区间为 k，所以左端点最多取到 n-k 的位置。

设定两个指针 left，right。left 指向 0，right 指向 n-k。

每次取 left 和 right 中间位置，判断 x 与左右边界的差值。x 与左边的差值为 x - arr[mid]，x 与右边界的差值为 arr[mid + k] - x。

如果 x 与左边界的差值 > x 与右边界的差值，即 x - arr[mid] > arr[mid + k] - x，将 left 右移，left = mid + 1，从右侧继续查找。
如果 x 与左边界的差值 <= x 与右边界的差值， 即 x - arr[mid] <= arr[mid + k] - x，则将 right 向左侧靠拢，right = mid，从左侧继续查找。
最后返回 arr[left, left + k] 即可。
'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = 0
        right = n - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left: left + k]