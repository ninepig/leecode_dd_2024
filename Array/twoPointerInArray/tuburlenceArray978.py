class Solution:
    '''
    湍流子数组实际上像波浪一样，比如 arr[i - 2] > arr[i - 1] < arr[i] > arr[i + 1] < arr[i + 2]。所以我们可以使用双指针的做法。具体做法如下：
使用两个指针 left、right。left 指向湍流子数组的左端，right 指向湍流子数组的右端。
如果 arr[right - 1] == arr[right]，则更新 left = right，重新开始计算最长湍流子数组大小。
如果 arr[right - 2] < arr[right - 1] < arr[right]，此时为递增数组，则 left 从 right - 1 开始重新计算最长湍流子数组大小。
如果 arr[right - 2] > arr[right - 1] > arr[right]，此时为递减数组，则 left 从 right - 1 开始重新计算最长湍流子数组大小。
其他情况（即 arr[right - 2] < arr[right - 1] > arr[right] 或 arr[right - 2] > arr[right - 1] < arr[right]）时，不用更新 left值。
更新最大湍流子数组的长度，并向右移动 right。直到 right >= len(arr) 时，返回答案 ans。
#代码
    '''
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 1
        ans = 1

        while right < len(arr):
            if arr[right - 1] == arr[right]:
                left = right
            elif right != 1 and arr[right - 2] < arr[right - 1] and arr[right - 1] < arr[right]:
                left = right - 1
            elif right != 1 and arr[right - 2] > arr[right - 1] and arr[right - 1] > arr[right]:
                left = right - 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans
