'''
If we have a string that is periodic (i.e. is made up of strings that are the same and repeat R times),
then we can check if the string is equal to some rotation of itself, and if it is, then we know that the string is periodic.
Checking if S is a sub-string of (S+S)[1:-1] basically checks if the string is present in a rotation of itself for all values of R such that 0 < R < len(S)
'''
'''
如果一个字符串是可以由子串repeated出来的
那我们只要不断rotate他 必然会有一个rotated过的string 和他相同
所以我们只要检查 s+s [1:-1] 之中是否还存在这个s 就知道他是否能组成了
太聪明了'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

       str_repeated= s + s

       return str_repeated.find(s) != -1