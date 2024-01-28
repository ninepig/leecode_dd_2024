class Solution:
    '''很好的题目

    关键是二分法的结构
            while left < right:
            mid = left + (right  - left) //2
            if arr[mid] < value:
                left = mid + 1
            else:
                right = mid

            我们的目标是 找到最左侧的index。 make sense 
    '''
    def findBestValue(self, arr: List[int], target: int) -> int:
        size = len(arr)
        arr.sort()
        # pre_sum array
        pre_sum = [0 for _ in range(size+1)]

        for i in range(size):
            pre_sum[i+1] = pre_sum[i] + arr[i]

        #算出  sum >= target 的最小value值
        value = self.binarySearchValue(arr,target,pre_sum)

        # 比较value 和 value -1
        sum_1 = self.calc_sum(arr, value, pre_sum)
        sum_2 = self.calc_sum(arr, value - 1 , pre_sum)
        diff_1 = abs(sum_1 - target)
        diff_2 = abs(sum_2 - target)

        return value if diff_1 < diff_2 else value - 1

    def binarySearchValue(self, arr, target, pre_sum):
        left, right = 0, arr[-1]
        while left < right:
            mid = left + (right - left) // 2
            if self.calc_sum(arr, mid, pre_sum) < target:
                left = mid + 1
            else:
                right = mid
        return left


    # 定位 value 的位置 用二分法  算出换成value以后的sum
    def calc_sum(self, arr, value, pre_sum):
        size = len(value)
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left) //2
            if arr[mid] < value:
                left = mid + 1
            else:
                right = mid
        return pre_sum[left] + (size - left) * value






