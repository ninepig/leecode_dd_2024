'''
217
 Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 1 hashset
 2 counting sort
 219
 Given an integer array nums and an integer k,
  return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

  出现距离 一般都会考虑hashmap 或者双指针。这个题肯定是hashmap 比较直观
 220
 比较复杂
 描述：给定一个整数数组 nums，以及两个整数 k、t。

要求：判断数组中是否存在两个不同下标的 i 和 j，其对应元素满足 abs(nums[i] - nums[j]) <= t，
同时满足 abs(i - j) <= k。如果满足条件则返回 True，不满足条件返回 False。
1brutal force
two loop
i
i -k i+ k
if exist num[i] - num[j] <= t

2 bucket sort  非常好的方法
'''
from bisect import bisect

from sortedcontainers import SortedList

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hset = set()
        # for idx in nums:
        #     if idx in hset:
        #         return True
        #     else:
        #         hset.add(idx)
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False

    def containsNearByDuplicate(self, nums: List[int], k:int) -> bool:
        arr_dict = dict()
        for i in range(len(nums)):
            if nums[i] in arr_dict and abs(i - arr_dict[nums[i]]) <= k :
                return True
            arr_dict[nums[i]] = i
        return False

    # o(n) space o(min(n,k))
    '''
    利用桶排序的思想，将桶的大小设置为 t + 1。只需要使用一重循环遍历位置 i，然后根据 nums[i] // (t + 1)，从而决定将 nums[i] 放入哪个桶中。
这样在同一个桶内各个元素之间的差值绝对值都小于等于 t。而相邻桶之间的元素，只需要校验一下两个桶之间的差值是否不超过 t。这样就可以以 
 的时间复杂度检测相邻 2 * k 个元素是否满足 abs(nums[i] - nums[j]) <= t。
而 abs(i - j) <= k 条件则可以通过在一重循环遍历时，将超出范围的 nums[i - k] 从对应桶中删除，从而保证桶中元素一定满足 abs(i - j) <= k。
具体步骤如下：

将每个桶的大小设置为 t + 1。我们将元素按照大小依次放入不同的桶中。
遍历数组 nums 中的元素，对于元素 nums[i] ：
如果 nums[i] 放入桶之前桶里已经有元素了，那么这两个元素必然满足 abs(nums[i] - nums[j]) <= t，
如果之前桶里没有元素，那么就将 nums[i] 放入对应桶中。
再判断左右桶的左右两侧桶中是否有元素满足 abs(nums[i] - nums[j]) <= t。
然后将 nums[i - k] 之前的桶清空，因为这些桶中的元素与 nums[i] 已经不满足 abs(i - j) <= k 了。
最后上述满足条件的情况就返回 True，最终遍历完仍不满足条件就返回 False。
'''
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket_dict = dict()
        for i in range(len(nums)):
            # put in bucket . bucket's interval is t
            num = nums[i] // (t + 1)

            # bucket already exist this num, t will only have 1 elemenet, otherwise it will already return true
            if num in bucket_dict:
                return True
            # put in bucket
            bucket_dict[num] = nums[i]

            # compare left bucket
            if num - 1 in bucket_dict and abs(bucket_dict[num - 1] - num[i]) <= t :
                return True

            # right bucket compare
            if num + 1 in bucket_dict and abs(bucket_dict[num + 1 ] - num[i]) <= t :
                return True

            # once interval bigger than k , removed bucket ,they can not be used to compare
            if i >= k :
                bucket_dict.pop(num[i-k] // (t+1))



        return False
    '''
    使用一个长度为 k 的滑动窗口，每次遍历到 nums[right] 时，滑动窗口内最多包含 nums[right] 之前最多 k 个元素。只需要检查前 k 个元素是否在 [nums[right] - t, nums[right] + t] 区间内即可。
检查 k 个元素是否在 [nums[right] - t, nums[right] + t] 区间，可以借助保证有序的数据结构（比如 SortedList）+ 二分查找来解决，从而减少时间复杂度。
具体步骤如下：

使用有序数组类 window 维护一个长度为 k 的窗口，满足数组内元素有序，且支持增加和删除操作。
left、right 都指向序列的第一个元素。即：left = 0，right = 0。
将当前元素填入窗口中，即 window.add(nums[right])。
当窗口元素大于 k 个时，即 right - left > k，移除窗口最左侧元素，并向右移动 left。
当窗口元素小于等于 k 个时：
使用二分查找算法，查找 nums[right] 在 window 中的位置 idx。
判断 window[idx] 与相邻位置上元素差值绝对值，若果满足 abs(window[idx] - window[idx - 1]) <= t 或者 abs(window[idx + 1] - window[idx]) <= t 时返回 True。
向右移动 right。
重复 3 ~ 6 步，直到 right 到达数组末尾，如果还没找到满足条件的情况，则返回 False。'''
    def containsNearbyAlmostDuplicateWindows(self, nums: List[int], k: int, t: int) -> bool:
        size = len(nums)
        left , right = 0 , 0
        windows = SortedList()

        while right < size:
            windows.add(nums[right])
            if right - left > k :
                windows.remove(nums[left])
                left += 1

            idx = bisect.bisect_left(windows,nums[right])

            if idx > 0 and abs(windows[idx] - windows[idx - 1]) <= t:
                return True

            if idx < len(windows) - 1 and abs(windows[idx] - windows[idx + 1] )<=t:
                return True

            right += 1

        return False