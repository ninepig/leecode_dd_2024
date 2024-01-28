from typing import List

'''
Brain question
only if all is 9 , we will do 100000
else we add 1 add the last digit


learning
python range (start, stop, step) 
stop could be negetive
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits.append(0)
        digits[0] = 1

        return digits