class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # num1 位数
        digit1 = len(num1) - 1
        # num2 位数
        digit2 = len(num2) - 1

        # 进位
        carry = 0
        # sum 存储反向结果
        sum = []
        # 逆序相加
        while carry > 0 or digit1 >= 0 or digit2 >= 0:
            # 获取对应位数上的数字
            num1_d = int(num1[digit1]) if digit1 >= 0 else 0
            num2_d = int(num2[digit2]) if digit2 >= 0 else 0
            digit1 -= 1
            digit2 -= 1
            # 计算结果，存储，进位
            num = num1_d+num2_d+carry
            sum.append('%d'%(num%10))
            carry = num // 10
        # 返回计算结果
        return "".join(sum[::-1])