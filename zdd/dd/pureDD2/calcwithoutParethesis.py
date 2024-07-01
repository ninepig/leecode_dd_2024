import math


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        preSign = '+'
        for c in s + '+': ## adding one more + to trigger last operator inside the loop
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop()*num)
                elif preSign == '/':
                    stack.append(stack.pop()//num) ## return integer part
                preSign = c
                num = 0
            else:
                continue
        return sum(stack)