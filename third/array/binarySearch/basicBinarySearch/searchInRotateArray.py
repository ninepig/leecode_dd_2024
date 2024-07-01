class Solution:
    '''
    z这个题的核心就是 画图
    num[right] 作为基准值
    然后看target 落在哪个区间里，然后毕竟
    '''
    def search(self, nums: List[int], target: int) -> int:
        ## santity check
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right] : ## on right side
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            elif nums[mid] == target:
                return mid
            else:
                if nums[mid]> target and target >= nums[left]:
                    right = mid -1
                else:
                    left = mid + 1

        return -1

## 如果有重复，和154一样。 不断逼近。
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[left]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] == target:
                    return True
                else:
                    left = left + 1

        return nums[left] == target
