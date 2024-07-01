class Solution:
    ''' todo 基数排序
    https://baike.baidu.com/item/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F'''
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