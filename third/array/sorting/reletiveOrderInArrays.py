'''
乐儿他从的1122
给你两个数组，arr1 和 arr2，arr2 中的元素各不相同，arr2 中的每个元素都出现在 arr1 中。

对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
'''
from typing import List


class Solution:
    '''
    counting sort
    数据规模比较小的情况下
    '''
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ## santity check
        res = []
        arr1_max = max(arr1)
        counter = [0 for _ in range(arr1_max)]

        for num in arr1:
            counter[num] += 1

        for num in arr2:
            while counter[num] != 0:
                res.append(num)
                counter[num] -= 1

        for num in counter:
            while counter[num] != 0:
                res.append(num)
                counter[num] -= 1

        return res


## 答案， 计数排序 计数的时候要减去min --》             counts[num - arr1_min] += 1
## 放回数组的时候 num = i + arr1_min
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 计算待排序序列中最大值元素 arr_max 和最小值元素 arr_min
        arr1_min, arr1_max = min(arr1), max(arr1)
        # 定义计数数组 counts，大小为 最大值元素 - 最小值元素 + 1
        size = arr1_max - arr1_min + 1
        counts = [0 for _ in range(size)]

        # 统计值为 num 的元素出现的次数
        for num in arr1:
            counts[num - arr1_min] += 1

        res = []
        for num in arr2:
            while counts[num - arr1_min] > 0:
                res.append(num)
                counts[num - arr1_min] -= 1

        for i in range(size):
            while counts[i] > 0:
                num = i + arr1_min
                res.append(num)
                counts[i] -= 1

        return res


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
sol = Solution()
print(sol.relativeSortArray(arr1,arr2))
