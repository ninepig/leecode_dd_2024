'''计算机的基本原理
只用管前两个数值
所以肯定是stack来做
'''


def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            stack.append(-stack.pop() + stack.pop())
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            stack.append(int(1 / stack.pop() * stack.pop()))
        else:
            stack.append(int(token))
    return stack.pop()