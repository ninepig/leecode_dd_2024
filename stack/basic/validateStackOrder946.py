class Solution:
    # 模拟题 这个类死脑筋急转弯 有影像就秒出
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        index = 0
        for item in pushed:
            s.append(item)
            while s and s[-1] == popped[index]:
                s.pop()
                index += 1

        return len(s) == 0 and index == len(popped) - 1