from bisect import bisect

from sortedcontainers import SortedList


class Solution:
    ''' 找是否有2个值 i， j  diff(i,j) <=k diff(num[i],num[j]) <=t
    固定windows +  windows内部sort '''

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        windows = SortedList()
        size = len(nums)
        left , right = 0 , 0
        while right < size:
            windows.append(nums[right])

            # 维护窗口小于k ， 用if 因为只可能出现再零界点，不会使用循环。
            if right - left > k:
                windows.remove(nums[left])
                left += 1

            # 找到右侧节点在windows的位置，因为是sorted
            rightIndex = bisect.bisect_left(windows,nums[right])

            # 比较和他最接近的2个数值，是否小于t
            if rightIndex < size - 1 and abs(windows[rightIndex + 1] - windows[rightIndex]) <= t:
                return True
            if right > 0 and abs(windows[rightIndex - 1] - windows[rightIndex]) <= t:
                return True

            right += 1

        return False