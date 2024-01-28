class Solution:
    '''纵向对比，很基本的字符串操作，多练习'''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        length = len(strs[0])
        count = len(strs)

        for i in range(0,length):
            c = strs[0][i]
            for j in range(1,count):
                if len(strs[j]) == i or c != strs[j][i]:
                    return strs[0][:i]

        return strs[0]