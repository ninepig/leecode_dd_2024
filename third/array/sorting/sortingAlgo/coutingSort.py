'''

https://algo.itcharge.cn/01.Array/02.Array-Sort/08.Array-Counting-Sort/#_3-%E8%AE%A1%E6%95%B0%E6%8E%92%E5%BA%8F%E4%BB%A3%E7%A0%81%E5%AE%9E%E7%8E%B0
时间复杂度 o（n+k）
用于整数排序

思想就是利用 数组 min max的值 生成一个辅助数组
然后统计在这个区间 数出现的次数
然后可以得到排序的index。 然后反向填充
这个要看实际应用


'''


class Solution:
    def countingSort(self, nums: [int]) -> [int]:
        # 计算待排序数组中最大值元素 nums_max 和最小值元素 nums_min
        nums_min, nums_max = min(nums), max(nums)
        # 定义计数数组 counts，大小为 最大值元素 - 最小值元素 + 1
        size = nums_max - nums_min + 1
        counts = [0 for _ in range(size)]

        # 统计值为 num 的元素出现的次数
        for num in nums:
            counts[num - nums_min] += 1

        # 生成累积计数数组
        for i in range(1, size):
            counts[i] += counts[i - 1]

        # 反向填充目标数组
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            # 根据累积计数数组，将 num 放在数组对应位置
            res[counts[num - nums_min] - 1] = num
            # 将 num 的对应放置位置减 1，从而得到下个元素 num 的放置位置
            counts[nums[i] - nums_min] -= 1

        return res

    def sortArray(self, nums: [int]) -> [int]:
        return self.countingSort(nums)
