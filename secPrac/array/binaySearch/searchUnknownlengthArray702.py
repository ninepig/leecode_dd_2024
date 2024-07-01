def read(right):
    pass


class Solution:
    # key point is how to know the length of array
    # we can try to use k to guess right bound and narrow left bound
    def search(self, reader, target):
        # locate right bound
        left = 0
        right = 1
        while read(right) < target:
            left = right
            right *= 2

        # binaery search with left, right

        # approaching way
        while left < right:
            mid = left + (right - left) // 2
            if read(mid) > target:
                left = mid + 1
            else:
                right = mid

        if read(left) == target:
            return left
        else:return - 1
