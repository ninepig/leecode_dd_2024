class Solution:
    '''类似计算机
    '''
    def decodeString(self, s: str) -> str:
        stack1 = []
        stack2 = []
        res = ""
        num = 0
        for c in s :
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '[':
                stack1.push(num)
                stack2.push(res)
                res = ""
                num = 0
            # 右括号代表需要计算
            elif c == ']':
                cur_res = stack2.pop()
                cur_num = stack1.pop()
                res = cur_res + res * cur_num
            else:
                res += c

        return res
