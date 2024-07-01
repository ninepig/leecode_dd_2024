class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                num = stack.pop() + stack.pop()
                stack.append(num)
            elif token == '-':
                num = stack.pop() + stack.pop()
                stack.append(num)
            elif token == '*':
                num = stack.pop() * stack.pop()
                stack.append(num)
            elif token == '/':
                num = 1/stack.pop() * stack.pop()
                stack.append(num)
            else:
                stack.append(int(token))

        return stack.pop()