class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # 算出presum ,利用presum + (size- left) * value  closed target  算出目标数组index
        # 双重二分法
        # 然后比较最接近的2个index , 算出最接近的值
        size = len(arr)
        arr.sort()
        pre_sum = [0 for _ in range(size + 1)]
        for i in range(size):
            pre_sum[i+1] = pre_sum[i] + arr[i]

        value = self.binarySearchValue(arr,pre_sum,target)

        sum1 = self.calcValue(arr,value,pre_sum)
        sum2 = self.calcValue(arr,value-1,pre_sum)
        diff_1 = abs(sum1 - target)
        diff_2 = abs(sum2 - target)

        return value if diff_1< diff_2 else value - 1

    def binarySearchValue(self, arr, pre_sum, target):
        left = 0
        right = arr[-1]
        while left < right:
            mid = left + (right - left) //2
            sum = self.calcValue(arr,mid,pre_sum)
            if sum < target:
                left = mid + 1
            else:
                right = mid
        return left

    ## 这部分可以用包来实现 bisection(arr,value)
    def calcValue(self, arr, value, pre_sum):
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) //2
            if arr[mid] < value:
                left = mid + 1
            else:
                right = mid

        return pre_sum[left] + (len(arr) - left) * value




