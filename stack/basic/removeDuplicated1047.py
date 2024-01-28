class Solution:
    '''经典栈题 熟悉python 操作'''
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in str:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
