class Solution(object):
    '''

    计算机系列 关键要明白一个核心
    遇到数值 累计
    遇到符号 计算,计算完了要入栈
    遇到括号 (入栈  /   )计算出栈
    '''
    def calculate(self, s):
        stack = []
        res = 0
        num = 0
        sign = 1
        for c in s:
            if c.isDigit():
                num = num*10 + int(c)
            # 如果是正负号 就把num 和 之前的和相加,重置正负号 以及当前num.等待下一个值
            elif c == '+' or c == '-':
                res += num * sign
                num = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res = res + sign*num
                num = 0
                res *= stack.pop()
                res += stack.pop()

        res += sign * num
        return res
    '''https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/medium/227.basic-calculator-ii
    另一种做法'''
    def calculate2_onstack(self, s: str) -> int:
        size = len(s)
        stack = []
        op = '+'
        index = 0
        while index < size:
            if s[index] == ' ':
                index += 1
                continue
            if s[index].isdigit():
                num = ord(s[index]) - ord('0')
                while index + 1 < size and s[index+1].isdigit():
                    index += 1
                    num = 10 * num + ord(s[index]) - ord('0')
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    top = stack.pop()
                    stack.append(top * num)
                elif op == '/':
                    top = stack.pop()
                    stack.append(int(top / num))
            elif s[index] in "+-*/":
                op = s[index]
            index += 1
        return sum(stack)

    ''' 因为有括号的存在, 所以必须op 和 当前 num 要分开 每个括号内 是一个num 然后括号外是一个op'''

    def calculate3(self, s):
        # Write your code here
        order = {'+': 0, '-': 0, '*': 1, '/': 1}
        stack = []
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            if c in '+-*/':
                while stack and stack[-1] != '(' and order[stack[-1]] >= order[c]:
                    op = stack.pop()
                    pre = stack.pop()
                    num = self.calc(pre, num, op)
                stack.append(num)
                stack.append(c)
                num = 0

            if c is '(':
                stack.append(c)

            if c is ')':
                while stack[-1] != '(':
                    op = stack.pop()
                    pre = stack.pop()
                    num = self.calc(pre, num, op)
                stack.pop()

        while stack:
            op = stack.pop()
            pre = stack.pop()
            num = self.calc(pre, num, op)

        return num

    def calc(self, a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a // b