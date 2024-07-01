class Solution:
    '''基本题'''
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        left , right = 0 , size - 1
        ans = 0
        while left < right:
            current_height = max(height[left],height[right])
            current_size = current_height *(right - left + 1)
            ans = max(ans,current_size)
            # 双指针的地方, 也可以不用双指针,一路怼过来. 就变成o(n2)了
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans