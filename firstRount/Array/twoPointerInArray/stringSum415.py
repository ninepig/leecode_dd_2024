'''
模拟数学题
双指针
python小技巧
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #store string result
        res = []
        sum , carry = 0, 0
        num1_index , num2_index = len(num1) - 1 , len(num2) - 1
        while carry > 0 or num1_index >0 or num2_index > 0:
            num1_digit = num1[num1_index] if num1_index > 0 else 0
            num2_digit = num2[num2_index] if num2_index > 0 else 0
            num2_index -= 1
            num1_index -= 1
            sum = num1_digit + num2_digit + carry
            res.append(sum%10)
            carry = sum / 10

        # python 语法真牛逼 reverse string
        return "".join(res[::-1])

