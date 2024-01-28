class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left , right = i + 1 , len(numbers) - 1
            while left < right:
                # 找到最左侧最适合的点
                mid = left + (right - left) // 2
                if numbers[mid] + numbers[i] < target:
                    left = mid + 1
                else:
                    right = mid
            if numbers[left] + numbers[i] == target:
                return [i+1, left + 1]

        return [-1,-1]