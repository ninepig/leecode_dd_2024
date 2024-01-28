class Solution:
    '''
    这道题的关键是理解的这个数组的形态
    也就是什么是波浪数组 up down up down up down 这种就是波浪数组
    所以双指针、dp 都可以 双指针清晰点
    '''
    # 本质就是滑动窗口
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        ret = 1
        left = right = 0

        while right < n - 1:
            if left == right:  # 特殊情况: 窗口长度为1
                if arr[left] == arr[left + 1]:  # 两指针相等时, 左右指针同时移动
                    left += 1
                right += 1  # 两指针不相等时, 只移动右指针
            else:  # 正常情况: 窗口长度不为1
                # 下面的两种情况下, 可以移动右指针扩大窗口
                if arr[right - 1] < arr[right] and arr[right] > arr[right + 1]:
                    right += 1
                elif arr[right - 1] > arr[right] and arr[right] < arr[right + 1]:
                    right += 1
                else:  # 不满足时,[left,right+1]也无法构成湍流子数组,直接将left移到right
                    left = right

            ret = max(ret, right - left + 1)
        return ret



    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        up = [1 for _ in range(N)]
        down =  [1 for _ in range(N)]
        res = 1
        for i in range(1, N):
            if arr[i - 1] < arr[i]:
                up[i] = down[i - 1] + 1
            elif arr[i - 1] > arr[i]:
                down[i] = up[i - 1] + 1
            res = max(res, max(up[i], down[i]))
        return res
