'''
经典backtrack
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        # path 的长度等于4 index 等于 s的长度的时候结束
        # 长度大于4 结束
        # 到下一层--》 append 新的current SUBstring
        # 循环之中加入大量剪枝
        def backtracking(index):
            if len(path) > 4:
                return
            if len(path) == 4 and index == len(s):
                res.append(''.join(path))
                return
            for i in range(index, len(s)):
                sub = s[index : i + 1] # current ip range

                if int(sub) > 255:
                    continue

                # 000 situation, skip
                if int(sub) == 0 and i != index:
                    continue
                 # 0xxx situation, skip
                if int(sub) > 0 and s[index] == '0':
                    continue

                path.append(sub)
                backtracking(index + 1)
                path.pop()

        backtracking(0)
        return res
