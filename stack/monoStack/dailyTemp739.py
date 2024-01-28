class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        dict = []
        ans = [0 for _ in range[len(T)]]
        for i in range(len(T)):
            # 单调递增栈, 虽然push的是index, 但是利用 index对应的value来
            while stack and T[i] > T[stack[-1]]:
                index = stack.pop()
                ans[index] = (i - index)
            stack.append(i)
        return ans