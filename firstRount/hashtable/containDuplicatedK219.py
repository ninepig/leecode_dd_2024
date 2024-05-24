class Solution:
    '''
    判断是否存在 num[i] == num[j]
    ，并且 i 和 j 的差绝对值至多为 k
    因为要看index的差距 所以不能排序
    1暴力法， 双层循环
    发现相同的 判断 i j 的距离
    2 hashtable
    值作为key index作为 value
    同样的值 加入table的时候 比较是否存在 diff(index) <= k , 如果存在 true 反之 取代value
    '''
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        htable = dict()
        for i in range(len(nums)):
            if nums[i] in htable:
                if abs(htable[nums[i]] - i) <= k:
                    return True
                else:
                    htable[nums[i]] = i
            htable[nums[i]] = i

        return False
    '''滑动数组的概念
    维护一个长度为k的hashtable
    利用出现次数来做 
    更直观'''
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = dict()
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return True
            nums_dict[nums[i]] = 1
            if len(nums_dict) > k:
    #python 删除hash key
                del nums_dict[nums[i - k]]
        return False