# https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/1296.%20%E5%88%92%E5%88%86%E6%95%B0%E7%BB%84%E4%B8%BA%E8%BF%9E%E7%BB%AD%E6%95%B0%E5%AD%97%E7%9A%84%E9%9B%86%E5%90%88.md
import collections

'''
需要自己做
'''
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        hand_map = collections.defaultdict(int)
        for i in range(len(nums)):
            hand_map[nums[i]] += 1
        for key in sorted(hand_map.keys()):
            value = hand_map[key]
            if value == 0:
                continue
            count = 0
            for i in range(k):
                hand_map[key + count] -= value
                if hand_map[key + count] < 0:
                    return False
                count += 1
        return True