class Solution:
    '''非递减排序，外加逼近'''
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        size = len(letters)
        left , right = 0 , size -1
        # ordered, so we try to find most left one
        while left < right:
             mid = left + (right - left) //2
             if left[mid] <= target:
                 left  = mid + 1
             else:
                 right = mid
       # if letter not exist
        return letters[left % size] # return most left letter

