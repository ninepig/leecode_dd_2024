class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = 0
        res = 0
        windows_sum = 0 ## 这里的windows不需要是数组，因为要求和，所以利用这一点 thread*k 就是windows的值
        while right < len(arr):
            windows_sum += arr[right]
            ## windows size
            if right - left + 1 >= k:
                if windows_sum >= k * threshold:
                    res += 1
                ## 缩小windows
                windows_sum -= arr[left]
                left += 1
            right += 1
        return res