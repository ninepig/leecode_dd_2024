class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            # skip if we have similar num[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right :
                while left < right and left > i + 1 and nums[left] == nums[left-1]:
                    left += 1
                while left < right and right < n - 1 and nums[right] == nums[right+1]:
                    right -= 1
                if left < right and nums[left] + nums[right] +nums[i] == 0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] +nums[i] > 0 :
                    right -= 1
                else:
                    left += 1

        return ans


    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        size = len(nums)
        for i in range(2, size):
            left = 0
            right = i - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if abs(total - target) < abs(res - target):
                    res = total
                if total < target:
                    left += 1
                else:
                    right -= 1

        return res

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        size = len(nums)
        res = 0
        for i in range(size):
            left, right = i + 1, size - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    res += (right - left)
                    left += 1
                else:
                    right -= 1
        return res