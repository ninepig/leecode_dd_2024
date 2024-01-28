class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        k_sum = 0
        left , right = 0 , 0
        count = 0
        size = len(arr)
        while right < size:
            # adding right,
            k_sum += arr[right]

            # fixed windows , when exceed k, remove left
            # when windows size is k, do the logic check
            if right - left + 1 >= k:
                if k_sum >= k*threshold:
                    count += 1
                k_sum -= arr[left]
                left += 1

            right += 1

        return count
