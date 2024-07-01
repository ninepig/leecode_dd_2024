from bisect import bisect

from sortedcontainers import SortedList


class Solution:
    #给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
    # basic, set can solve problem
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False

    '''
    给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
    如果存在，返回 true ；否则，返回 false 
    '''
    # complexDs store num:index pairs
    '''
    维护一个最多有 k 个元素的哈希表。遍历 nums，对于数组中的每个整数 nums[i]，判断哈希表中是否存在这个整数。

    如果存在，则说明出现了两次，且 
    ，直接返回 True。
    
    如果不存在，则将 nums[i] 加入哈希表。
    
    判断哈希表长度是否超过了 k，如果超过了 k，则删除哈希表中最旧的元素 nums[i - k]。
    
    如果遍历完仍旧找不到，则返回 False'''
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap= dict()
        ##自己的做法 需要不断维护同一个值的value, 比较麻烦,因为idx是逐渐变大的
        for idx,value in enumerate(nums):
            if value in hashmap:
                if abs(hashmap[value] - idx) <= k:
                    return True
                else:
                    hashmap[value] = idx # update index
            else:
                hashmap[value] = idx # set index

        return False

    # 这个做法更简单一点.好理解,需要用删掉这个操作,也利用了dict的性质
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        nums_dict = dict()
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return True
            nums_dict[nums[i]] = 1
            if len(nums_dict) > k:
                del nums_dict[nums[i - k]]
        return False


    '''
    给你一个整数数组 nums 和两个整数 indexDiff 和 valueDiff 。

    找出满足下述条件的下标对 (i, j)：
    i != j,
    abs(i - j) <= indexDiff
    abs(nums[i] - nums[j]) <= valueDiff
    利用一个sortedList 的windows 来做
    每个num 放入其中
    
    '''
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        windows = SortedList()
        left = 0
        right = 0
        size = len(nums)

        while right < size:
            windows.add(nums[right])
            if right - left > indexDiff:
                windows.remove(nums[left])
                left += 1

            idx = bisect.bisect_left(windows, nums[right])

            if idx > 0 and abs(windows[idx] - windows[idx - 1]) < valueDiff:
                return True
            if idx > 0 and abs(windows[idx + 1] - windows[idx]) < valueDiff:
                return True

            right += 1

        return False
