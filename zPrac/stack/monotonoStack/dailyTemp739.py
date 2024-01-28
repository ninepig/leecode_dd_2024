from LinkedList import List


class Solution:
    # 单调栈内存 index, 用index指向数组
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for _ in range(len(T))]
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                index = stack.pop(-1)
                #这里需要插入对应的index
                res[index] = i - index
            stack.append(i) # 加入index即可.递增栈
        return res

