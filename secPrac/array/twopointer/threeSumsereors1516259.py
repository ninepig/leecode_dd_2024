class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        nums.sort()
        res = []
        for i in range(size):
            if i > 0 and nums[i-1] == nums[i]:
                continue  ## removed duplated
            left = i + 1
            right = size - 1
            while left < right:
                ## 去重
                while left < right and left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and right < size - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                if nums[left] + nums[right] + nums[i] == 0:
                    res.append([nums[left],nums[i],nums[right]])
                    left -= 1
                    right += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                else:
                    left +=1
        return res

        # 找所有方案 所以不需要去重, 所以循环判断的时候最终条件的时候 right - left 之间所有的数都满足
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        size = len(nums)
        nums.sort()
        ans = 0
        for i in range(size):
            left = 0
            right = size -1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    ans += (right - left)
                    left += 1
                else:
                    right -= 1
        return ans

      '''题目中说了 只有一组解 所以很明显 不需要去重'''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        nums.sort()
        res = float('inf')
        for i in range(size):
            left = i + 1
            right =  size - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                ## 判断 从等于变成了判断
                if abs(total - target) < abs(res -target):
                    res = total
                # 毕竟 对撞过程
                if total > target:
                    right -= 1
                else:
                    left +=1

        return res

    def fourSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        nums.sort()
        res = []
        for i in range(size):
            if i > 0 and nums[i - 1] == nums[i]:
                continue  ## removed duplated
            for j in range(i+1, size):
                if j > i and nums[j - 1] == nums[j]:
                    continue  ## removed duplated
                left = j + 1
                right = size - 1
                while left < right:
                    ## 去重
                    while left < right and left > j + 1 and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and right < size - 1 and nums[right] == nums[right + 1]:
                        right -= 1
                    if nums[left] + nums[right] + nums[i] + nums[j] == 0:
                        res.append([nums[left], nums[i], nums[right]],nums[j])
                        left -= 1
                        right += 1
                    elif nums[left] + nums[right] + nums[i] + nums[j]> 0:
                        right -= 1
                    else:
                        left += 1
        return res