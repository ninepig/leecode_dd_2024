'''
面经题
'''
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        res = 0
        length = len(heights)
        for i in range(length):
            cur_height = heights[i]
            ## find left which higher than cur_height
            left , right = i  , i
            ## > 0 因为 left -=1
            while left > 0 and cur_height <= heights[left]:
                left -= 1
            ## < length - 1 / right += 1
            while right < length - 1 and heights[right] >= cur_height:
                right += 1
            res = max(res, cur_height *  (right - left + 1))

        return  res

    def largestRectangleAreaStack(self, heights: list[int]) -> int:
        res = 0
        heights.append(0) ## add dummy node on right, so we can check last height in the array
        length = len(heights)
        stack = []
        for i in range(length):
            while stack and heights[i] < heights[stack[-1]]:## we found one element smaller than top on stack
                current_element = stack.pop() ## top of the stack
                if stack :
                    left_index = stack[-1] + 1  ## + 1 means we need right side of the histgram
                else:
                    left_index = 0 ## if stack emtpty , means we arrvide leftest
                right_index = i - 1
                res = max(res, (right_index - left_index + 1 ) * heights[current_element])
            stack.append(i) ## push into stack
        return  res