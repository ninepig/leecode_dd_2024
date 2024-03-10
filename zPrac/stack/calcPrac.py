class solution:
    def calcParetheisAddMinusOnly(self, s: str)->int:
        ## corner case handling:
        preSign = 1
        stack = []
        num , res = 0, 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                res += preSign * num
                num = 0
                preSign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(res)
                #  we must have + - before parathesis, first sign is +
                stack.append(preSign)
                preSign = 1 ## we need reset this
                res = 0 ## we need also push res into stack
            elif c == ')':
                res += num * preSign ## 内部是+= ！！！
                res *= stack.pop() ## pop out sign and times with value inside of para
                res += stack.pop() ## adding previous value
                num = 0
            else:
                continue
        ## just incase we missed last digit
        return res + num * preSign


    def calcWithoutPareth(self,s:str)->int:
        preSign = '+'
        stack = []
        num = 0
        for c in s + '+': ## adding "+" to make sure there is no num left
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if preSign == '+': # check previous sign
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                elif preSign == '/':
                    stack.append(stack.pop()//num)
                ## reset number and sign after calc
                preSign = c
                num = 0
            else:
                continue

        return sum(stack)


    def calcEverything(self,s:str)->int:
        order = {'+':0,'-':0 , '*':1,'/':1}
        stack = []
        num = 0
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c in "+-*/":
                ## check if we have different order of op
                ## 1 not ( 2 stack top's ops order is higher than current one
                while stack and stack[-1] != '(' and order[stack[-1]] > order[c]:
                    ops = stack.pop()
                    pre = stack.pop()
                    num = self.calc(pre,num,ops)
                stack.append(num) #push what we have
                stack.append(c) # push current sign
                num = 0 ## reset num
            elif c == "(":
                stack.append(c)
            elif c == ")":
                while stack[-1] != '(': ## calc this parethsis
                    ops = stack.pop()
                    pre = stack.pop() ## pop the pre number
                    num = self.calc(pre,num,ops)
                stack.pop() ## pop the left (
                ## 括号完了肯定是一个符号，所以不需要reset num， 会再下一次计算后reset
            else:
                continue
        while stack:
            ops = stack.pop()
            pre = stack.pop()
            num = self.calc(pre,num,ops)

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