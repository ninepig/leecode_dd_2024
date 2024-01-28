'''
分割过程：先递归地将当前序列平均分成两半，直到子序列长度为 1。
找到序列中心位置 mid，从中心位置将序列分成左右两个子序列 left_arr、right_arr。
对左右两个子序列 left_arr、right_arr 分别进行递归分割。
最终将数组分割为 n 个长度均为 1 的有序子序列。
归并过程：从长度为 1 的有序子序列开始，依次进行两两归并，直到合并成一个长度为 n 的有序序列。
使用数组变量 arr 存放归并后的有序数组。
使用两个指针 left_i、right_i 分别指向两个有序子序列 left_arr、right_arr 的开始位置。
比较两个指针指向的元素，将两个有序子序列中较小元素依次存入到结果数组 arr 中，并将指针移动到下一位置。
重复步骤 3，直到某一指针到达子序列末尾。
将另一个子序列中的剩余元素存入到结果数组 arr 中。
返回归并后的有序数组 arr。
'''
class Solution:
    def mergeSort(self,arr):
        if len(arr) <= 1 :
            return arr

        mid = len(arr) // 2
        left_arr = self.mergeSort(arr[0:mid])
        right_arr = self.mergeSort(arr[mid:])
        return self.merge(left_arr,right_arr)

    def merge(self,left_arr,right_arr):
        arr = []
        left_i, right_i = 0, 0
        # 左右侧 list 比较大小， 靠小的加入list
        while left_i < len(left_arr) and right_i < len(right_arr):
            if left_arr[left_i] < right_arr[right_i]:
                arr.append(left_arr[left_i])
                left_i += 1
            else:
                arr.append(right_arr[right_i])
                right_i += 1

        while left_i < len(left_arr):
            arr.append(left_arr[left_i])
            left_i += 1

        while right_i < len(right_arr):
            arr.append(right_arr[right_i])
            right_i+=1

        return arr