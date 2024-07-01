class Solution:
    '''画图, 只有两种可能性 同153 154'''
    # 这个题因为只存在一个确定解 ,所以不需要去重
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left , right = 0 , size - 1
        ## get number directly
        while left <= right :
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > left : # left side (in spin condition)
                if  nums[left ]<= target < nums[mid]: # left of left side
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right side (in spin condition)
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

## judge if exist, 因为有重复值,需要去重
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
                ## 存在, 如果不存在 就继续搜索. 因为可能重复 所以 mid == left得情况会出现, 所以让left ++ 进行下列一轮循环同时去重
                if nums[mid] == target:
                    return True
                else:
                    left = left + 1

        return nums[left] == target