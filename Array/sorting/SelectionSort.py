'''
选择排序算法步骤 #
第 1 趟排序：
无已排序部分，把第 1 ~ n 个元素（总共 n 个元素）作为未排序部分。
遍历 n 个元素，使用变量 min_i 记录 n 个元素中值最小的元素位置。
将 min_i 与未排序部分第 1 个元素（也就是序列的第 1 个元素）交换位置。如果未排序部分第 1 个元素就是值最小的元素位置，则不用交换。
此时第 1 个元素为已排序部分，剩余第 2 ~ n 个元素（总共 n - 1 个元素）为未排序部分。
第 2 趟排序：
遍历剩余 n - 1 个元素，使用变量 min_i 记录 n - 1 个元素中值最小的元素位置。
将 min_i 与未排序部分第 1 个元素（也就是序列的第 2 个元素）交换位置。如果未排序部分第 1 个元素就是值最小的元素位置，则不用交换。
此时第 1 ~ 2 个元素为已排序部分，剩余第 3 ~ n 个元素（总共 n - 2 个元素）为未排序部分。
依次类推，对剩余 n - 2 个元素重复上述排序过程，直到所有元素都变为已排序部分，则排序结束。
'''

class Solution:
    def selectionSort(self, arr):
        for i in range(len(arr) - 1):
            # 记录未排序部分中最小值的位置
            min_i = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_i]:
                    min_i = j
            # 如果找到最小值的位置，将 i 位置上元素与最小值位置上的元素进行交换
            if i != min_i:
                arr[i], arr[min_i] = arr[min_i], arr[i]
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.selectionSort(nums)