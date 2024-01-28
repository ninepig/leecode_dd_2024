class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # find peak
        # search on onhill  asceding order
        # search on downhill descding order
        peak_pos = self.findPeak(mountain_arr)
        uphill_pos = self.findTargetInuphill(target,0,peak_pos)
        downhill_pos = self.findTargetIndownhill(target,peak_pos,len(mountain_arr) - 1)
        return uphill_pos if uphill_pos != -1 else downhill_pos

    def peak(self):
        pass

    def findPeak(self, mountain_arr):
        left = 0
        ans = 0
        right = len(mountain_arr) - 1 # get len api
        while left <= right:
            mid = left + (right - left) // 2
            if self.peak(mid - 1) < self.peak(mid) > self.peak(mid + 1):
                ans = mid
                break # answer exit, so we use break to make function good
            if self.peak(mid) < self.peak(mid + 1): # uphill, peak on right
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def findTargetInuphill(self, target, start, peak_pos):
        # uphill
        left = start
        right = peak_pos
        # find most left value ,approching method
        while left < right :
            mid = left + (right - left) // 2
            if self.peak(mid) < target:
                left = mid + 1
            else:
                right = mid
        return left if self.peak(left) == target else -1


    def findTargetInDownhill(self, target, start, peak_pos):
        # Down
        left = start
        right = peak_pos
        # find most left value ,approching method
        while left < right :
            mid = left + (right - left) // 2
            if self.peak(mid) > target:
                left = mid + 1
            else:
                right = mid
        return left if self.peak(left) == target else -1



