class Solution:
    # ( append index to stack
    # ) pop stack, if stack ' top is ( (not empty) , we have valid pairs, update ans
    # if stack is empty, means, is not valid, we push this as a dummy pos
    # we keep 1 element in stack dummy element meaning-> 最长有效括号子串的开始元素的前一个元素下标
    # distance = right) pos - dummy element
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # dummy element
        ans = 0
        for index,val in enumerate(s):
            if val == '(':
                stack.append(index)
            else:
                stack.pop()# pop valid parethesis
                if stack: # has element
                    ans = max(ans, index - stack.pop())
                else: # no element, means no pair fund, push another dummy node
                    stack.append(index)

        return ans 

