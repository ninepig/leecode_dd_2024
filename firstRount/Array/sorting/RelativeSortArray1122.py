from typing import List

'''
描述：给定两个数组，arr1 和 arr2，其中 arr2 中的元素各不相同，arr2 中的每个元素都出现在 arr1 中。

要求：对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
'''
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_min = min(arr1)
        arr1_max = max(arr1)
        size = arr1_max - arr1_min + 1
        count = [0 for _ in range(size)]

        # Count what in arr1
        for num in arr1:
            count[num - arr1_min] += 1

        # based on arr2 to get relative order in arr1
        res = []

        for num in arr2:
            while count[num - arr1_min] > 0:
                res.append(num)
                count[num - arr1_min] -= 1

        # put rest in to array , in asc order in arr1
        for i in range(size):
            while count[i] > 0 :
                res.append(i + arr1_min)
                count[i] -= 1

        return res