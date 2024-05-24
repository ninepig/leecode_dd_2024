'''
这道题的关键点在于找到数组的大小，以便确定查找的右边界位置。右边界可以通过倍增的方式快速查找。
在查找右边界的同时，也能将左边界的范围进一步缩小。等确定了左右边界，就可以使用二分查找算法快速查找 target。
'''
class Solution:
    def binarySearch(self, reader, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if target > reader.get(mid):
                left = mid + 1
            else:
                right = mid
        if reader.get(left) == target:
            return left
        else:
            return -1

    def search(self, reader, target):
        left = 0
        right = 1
        while reader.get(right) < target:
            left = right
            right <<= 1

        return self.binarySearch(reader, left, right, target)