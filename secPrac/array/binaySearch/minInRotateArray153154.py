class Solution:
    '''对于旋转数组 只有两种可能, 因为是升序
          *
        *
      *
    *
  *
*
    *
  *
*
          *
        *
      *
      所以最小值 第一种情况是最左侧
      第二种情况是 第二段的最左侧, 所以我们里用排除法,focus在左侧即可

    '''
    ## focus 在找最左侧, 所以用排除法
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        left, right = 0 , size - 1
        while left < right:
            mid = left +(right - left) //2
            if nums[mid] > nums[right]: # 找spin得点
                left = mid + 1
            else:
                right = mid
        return nums[left]

    ## 154 , 要去重, 因为出现了 num[mid] == nums[right] 的情况, 所以不断向左缩小范围
    def findMinDuplicated(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right = right - 1
        return nums[left]