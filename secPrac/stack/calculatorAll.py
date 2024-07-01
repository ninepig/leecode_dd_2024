'''计算机系列里
sign用来保存在这个当前num 前面的运算符
stack放运算符(一个栈) + 计算好的值(非常重要, 有括号的情况,需要把值入栈), 然后用一个外部元素维护最终结果
比如 4 * 3 , 第一个sign是+ ,第二个sign是3 , stack之中保存的是+ 4 * 3, 我们需要出栈来获取符号,或者利用sign来获取这个符号  '''



class Solution:
    # one stack
    # 字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格。 整数除法仅保留整数部分
    def calculate2(self, s: str) -> int:
        sign = '+'
        stack = []
        cur_num = 0

        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                ## 我们已经知道sign了. 所以在这里如果一单出现符号,要计算之前已经有的值,因为要替换新的付好了
                if sign == '+':
                    stack.append(cur_num)
                elif sign == '-':
                    stack.append(-cur_num)
                elif sign == '*':
                    tmp = stack.pop()
                    stack.append(tmp*cur_num)
                elif sign == '/':
                    tmp = stack.pop()
                    stack.append(int(tmp/cur_num))
                #after process
                cur_num = 0
                sign = c # assign new value to sign
        return sum(stack)

    ## 括号 + 正负符号
    # 正负符号, 计算
    # ( 入栈
    # ) 计算, 同时要出栈计算
    # 这个方法不太好,写的
    def calculate1bad(self, s: str) -> int:
        pass
        # stack = []
        # res = 0
        # cur_num = 0
        # pre_sign = "+" # 用正负不好, 写起来比较麻烦
        #
        # for c in s:
        #     if c == ' ':
        #         continue
        #     elif c.isdigit():
        #         cur_num = cur_num * 10 + c
        #     elif c in "+-": # if current is + or -
        #         cur_num = cur_num if pre_sign == "+" else -cur_num
        #         res += cur_num
        #         cur_num = 0 # reset cur num
        #         pre_sign = c # assign current sign to pre_sign
        #     elif c == '(':
        #         stack.append(res) # append current value
        #         stack.append(pre_sign) # append current sign
        #         res = 0
        #         pre_sign = "+"
        #     elif c == ')':
        #         # 计算当前括号内的值, 也就是把sign 和 num 和sign处理 类似(+ , -)的处理, 再加上 括号的逻辑,也就是计算出栈逻辑
        #         cur_num = cur_num if pre_sign == "+" else -cur_num
        #         res += cur_num
        #         temp_sign = stack.pop()
        #         temp_num = stack.pop()
        #         res = res if temp_sign == "+" else -res
        #         res = temp_num + res
        #
        # cur_num = cur_num if pre_sign == "+" else -cur_num
        # res += cur_num
        #
        # return  res

    # better method
    # 写的好的方法
    def calculate1(self, s: str) -> int:
        pre_sign = 1 # 1 means + , -1 means -
        res = 0
        cur_num = 0
        stack = []

        for c in s :
            if c == ' ':
                continue
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c in "+-":
                res += cur_num*pre_sign
                pre_sign = 1 if c == '+' else -1
                cur_num = 0
            elif c == '(':
                stack.append(res)
                stack.append(pre_sign)
                pre_sign = 1
                res = 0 # need reset res to 0 , need cal what in parethesis
            elif c == ')':
                res += cur_num * pre_sign # get res in paretheis
                cur_num = 0
                res *= stack.pop() # get sign for number in parethere
                res += stack.pop() # calc them together

        res += pre_sign * cur_num # see if we have something left

        return res

    def calculate3(self, s):
      order = {'+':0,'-':0,'*':1,'/':1} # dict for order of ops, which let * / has high priority
      stack = []
      num = 0
      # we dont need pre_sign in this question, default is + , since we left all cal in the end
      for c in s:
          if c.isdigit():
              num = num * 10 + int(c)
          elif c == ' ':
              continue
          elif c in '+-*/':
              while stack and stack[-1] != '(' and order[stack[-1]] >= order[c]:
                  # 当遇到当前是* / 之前是 +- 的情况, 我们不计算先前的,直接入栈,因为要保证先做*/
                  # 同时计算括号内所有的值
                  ops = stack.pop()
                  pre = stack.pop()
                  num = self.calc(pre,num,ops)
              stack.append(num)
              stack.append(c)
          elif c == '(':
             stack.append(c)
          elif c == ')':
              while stack[-1] != '(':
                  ops = stack.pop()
                  pre = stack.pop()
                  num = self.calc(pre,num,ops)
              stack.pop() # remove (
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