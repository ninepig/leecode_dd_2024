'''
思路 1：基数排序 #
这道题的难点在于要求时间复杂度和空间复杂度为
。

这道题分为两步：

数组排序。
计算相邻元素之间的差值。
第 2 步直接遍历数组求解即可，时间复杂度为
。所以关键点在于找到一个时间复杂度和空间复杂度为
 的排序算法。根据题意可知所有元素都是非负整数，且数值在 32 位有符号整数范围内。所以我们可以选择基数排序。基数排序的步骤如下：

遍历数组元素，获取数组最大值元素，并取得位数。
以个位元素为索引，对数组元素排序。
合并数组。
之后依次以十位，百位，…，直到最大值元素的最高位处值为索引，进行排序，并合并数组，最终完成排序。
最后，还要注意数组元素个数小于 2 的情况需要特别判断一下。
'''
class Solution:
    def radixSort(self, arr):
        size = len(str(max(arr)))

        for i in range(size):
            buckets = [[] for _ in range(10)]
            for num in arr:
                buckets[num // (10 ** i) % 10].append(num)
            arr.clear()
            for bucket in buckets:
                for num in bucket:
                    arr.append(num)

        return arr

    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        arr = self.radixSort(nums)
        return max(arr[i] - arr[i - 1] for i in range(1, len(arr)))