class Solution:
    def calculate3(self, s):
        # Write your code here
        order = {'+': 0, '-': 0, '*': 1, '/': 1}
        stack = []
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            if c in '+-*/':
                ## 找到栈顶符号 是否和当前符号不是同一个级别 比如当前是+ - 栈顶是 * / 先把扎顶计算了， 也就是先做乘除法， 目标是让stack之中的 符号都处于同一级别。 这样就可以顺序计算。
                while stack and stack[-1] != '(' and order[stack[-1]] >= order[c]:
                    op = stack.pop()
                    pre = stack.pop()
                    num = self.calc(pre, num, op)
                stack.append(num)
                stack.append(c)
                num = 0

            if c is '(':
                stack.append(c)

            ## 找到对应括号内容 并进行计算。
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