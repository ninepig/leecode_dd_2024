class Solution:
    '''
    类似计算题, 出现[ 要把之前的值全部入栈, 出现] 要计算当前括号内的值
    输入：s = "3[a2[c]]"
    输出："accaccacc"'''
    def decodeString(self, s: str) -> str:
        num_stack = []
        char_stack = []
        res = ""
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[': # push all current char and num in to stack
                num_stack.append(num)
                char_stack.append(res)
                res = ""
                num = 0
            elif c ==']': #
                cur_num = num_stack.pop()
                pre_res = char_stack.pop()
                res = pre_res + res * cur_num
            else:
                res += c # current res

        return res
