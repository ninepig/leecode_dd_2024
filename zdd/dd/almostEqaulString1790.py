import collections


class Solution:

    ## 用额外的空间而已..效率还是很好的 也很好理解
    def areAlmostEqualBrutalForce(self, s1: str, s2: str) -> bool:
        counter1 = collections.Counter(s1)
        counter2 = collections.Counter(s2)
        if counter1 != counter2:
            return False
        count  = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
            if count > 2:
                return False

        if count ==0 or count == 2:
            return True
        return False

    ## 不需要用couter 根据题意进行模拟即可 : 使用 a 和 b 记录不同的位置下标，初始值为 -1，
    # 若「不同位置超过 222 个」或「只有 111 个」直接返回 false，若「不存在不同位置」或「不同位置字符相同」，则返回 true。

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n, a, b = len(s1), -1, -1
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            if a == -1:
                a = i
            elif b == -1:
                b = i
            else: ## more than 3 times
                return False
        ## 0 times
        if a == -1:
            return True
        ## 1 times
        if b == -1:
            return False
        ## to see if they can swap
        return s1[a] == s2[b] and s1[b] == s2[a]

    # 作者：宫水三叶
    # 链接：https: // rareleetcode.cn / problems / check - if -one - string - swap - can - make - strings - equal / solutions / 1883347 / by - ac_oier - qeul /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        ## 更直接点
    def areAlmostEqual2(self, s1: str, s2: str) -> bool:
        cnt = 0
        c1 = c2 = None
        for a, b in zip(s1, s2):
            if a != b:
                cnt += 1
                if cnt > 2 or (cnt == 2 and (a != c2 or b != c1)):
                    return False
                c1, c2 = a, b
        return cnt != 1

    # 作者：ylb
    # 链接：https: // rareleetcode.cn / problems / check - if -one - string - swap - can - make - strings - equal / solutions / 1 / by - lcbin - dy58 /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。