import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = collections.Counter(s)
        counter2 = collections.Counter(t)

        return counter1 == counter2

# 同构题
# 输入：s = "egg", t = "add"
# 输出：True
class SolutionA:
    def isIsomorphic(self, s: str, t: str) -> bool:
        counter1 = collections.Counter(s)
        counter2 = collections.Counter(t)
        # print(counter1.values())
        # print(counter2.values())
        value1 = sorted(list(counter1.values()))
        value2 = sorted(list(counter2.values()))
        # print(value1)
        # print(value2)
        return value1 == value2

    # pair to pair,so we need compare them one by one and store mapping from s to t and t to s
    def isIsomorphicAnswer(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        for i in range(len(s)):
            if s[i] in s_dict and s_dict[s[i]] != t[i] : # not mapping
                return False
            if t[i] in t_dict and t_dict[t[i]] != s[i] : #not mapping
                return False
            s_dict[s[i]] = t[i]
            t_dict[t[i]] = s[i]

        return True



test = SolutionA()
test.isIsomorphic("abc","doo")
