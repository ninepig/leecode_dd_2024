class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0 :
            return ""
        length = len(strs[0])
        count = len(strs)
        for i in range(length):
            char_firststring = strs[0][i]
            for j in range(1,count):
                if len(strs[j]) == i or  strs[j][i] != char_firststring :# substring length same or not comman prefix
                    return strs[0][:i]

        return strs[0] # all string same