class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = dict()
        # counter = Couter(s) python 自带的包
        for c in str:
            counter[c] = counter.getDefault(c,0) + 1
        flag = -1
        # python complexDs 的loop 是value ，然后需要自己取值
        for key in counter:
            if flag == -1 :
                flag = counter[key]
            else:
                if flag != counter[key]:
                    return False

        return True