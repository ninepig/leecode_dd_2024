class Solution:
    '''经典题'''
    def addStrings(self, num1: str, num2: str) -> str:
        right = len(num1) - 1
        right2 = len(num2) - 1
        sum_array = []
        carry = 0
        while right >= 0 and right2 >=0:
            digit1 = int(num1.index(right)) if right >=0 else 0 ## 非常好的判斷
            digit2 = int(num2.index(right2)) if right2 >= 0 else 0  ## 非常好的判斷 這樣就不需要再額外的循環了
            cur_sum = digit1 + digit2 + carry
            carry = cur_sum // 10
            digit_cur = cur_sum % 10
            sum_array.append(digit_cur)

        if carry != 0:
            sum_array.append(carry)

        return "".join(sum_array[::-1])



