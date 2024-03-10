class Solution:
    '''
    We only have  + -  （ ）
    Using stack to do this
    when we see + or -
    mean, we can calulater previous result
    then get new sign
    6 + 5 -4 -》 first sign is +6 , we see second + , so we get res = 6
    we see (
    we can push the revious result into stack
    we also store previous sign into stack .
    new sign is + (which is 1)
    new res = 0
    when we see )
    we first cal the current res inside the parethesis
    then pop out the stack

    '''
    def calculate(self, s: str) -> int:
        num = 0
        sign = 1
        res = 0
        stack = []
        for c in s: # iterate till last character
            # c = s[i]
            if c.isdigit(): # process if there is digit
                num = num*10 + int(c) # for consecutive digits 98 => 9x10 + 8 = 98
            elif c in '-+': # check for - and +
                res += num*sign
                sign = -1 if c == '-' else 1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res +=sign*num
                res *=stack.pop()
                res +=stack.pop()
                num = 0
        return res + num*sign


class Solution:
    def calculate(self, s: str) -> int:

        def recurs(s, start):
            operand = result = 0
            nextSign = 1  # 1 for positive, -1 for negative (used to change sign of operand since we're always adding)
            i = start
            while i < len(s) - 1:
                i += 1
                c = s[i]

                if c == " ":
                    continue

                if c.isdigit():
                    # add digit to operand (could be multiple)
                    operand = 10 * operand + int(c)
                elif c == "(":
                    # new sub-expression - recurs
                    end, operand = recurs(s, i)
                    i = end
                elif c == ")":
                    # sub-expression ended - exit
                    break
                else:
                    # operator
                    result += nextSign * operand
                    nextSign = 1 if c == "+" else -1
                    operand = 0

            return i, result + (nextSign * operand)

        return recurs(s, -1)[1]
