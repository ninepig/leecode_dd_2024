class Solution:
    '''
    从下标为 0 开头的子串回溯。

对于下标为 index 开头的子串，我们可以在 index + 1 开始到 len(s) - 1 的位置上，分别进行子串拆分，将子串拆分为 s[index: i + 1]。

如果当前子串不在 s_set 中，则将其存入 s_set 中，然后记录当前拆分子串个数，并从 i + 1 的位置进行下一层递归拆分。然后在拆分完，对子串进行回退操作。

如果拆到字符串 s 的末尾，则记录并更新 ans。

在开始位置还可以进行以下剪枝：如果剩余字符个数 + 当前子串个数 <= 当前拆分后子字符串的最大数目，则直接返回。
    '''
    def maxUniqueSplit(self, s: str) -> int:
        helper_set = set()
        ans = 0
        def backtrack(index,count):
            nonlocal ans # 访问函数外变量
            # trim process
            # 在开始位置还可以进行以下剪枝：如果剩余字符个数 + 当前子串个数 <= 当前拆分后子字符串的最大数目，则直接返回
            if len(s) - index + count < ans:
                return
            if index > len(s):
                ans = max(ans,count)
                return
            for i in range(index,len(s)):
                sub_s = s[index : i + 1]
                if sub_s not in helper_set:
                    helper_set.add(sub_s)
                    backtrack(i + 1, count + 1)
                    helper_set.remove(s)
        backtrack(0,0)
        return ans


class SolutionAns:
    ans = 0
    def backtrack(self, s, index, count, s_set):
        if len(s) - index + count <= self.ans:
            return
        if index >= len(s):
            self.ans = max(self.ans, count)
            return

        for i in range(index, len(s)):
            sub_s = s[index: i + 1]
            if sub_s not in s_set:
                s_set.add(sub_s)
                self.backtrack(s, i + 1, count + 1, s_set)
                s_set.remove(sub_s)


    def maxUniqueSplit(self, s: str) -> int:
        s_set = set()
        self.ans = 0
        self.backtrack(s, 0, 0, s_set)
        return self.ans