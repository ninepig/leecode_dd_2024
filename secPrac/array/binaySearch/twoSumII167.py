class Solution:
    # 对撞指针 传统做法o(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

    # 二分法 o(nlogN) 最坏, 还不如用对撞指针
    def twoSumBinarySearch(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                mid = left + (right - left) // 2
                if numbers[mid] + numbers[i] < target:
                    left = mid + 1
                else:
                    right = mid
            if numbers[left] + numbers[i] == target:
                return [i + 1, left + 1]

        return [-1, -1]