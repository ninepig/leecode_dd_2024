## 脑筋急转弯

## https://leetcode.cn/problems/split-message-based-on-limit/solutions/1964660/mei-ju-fen-duan-de-shu-liang-mo-ni-by-ne-ajk1
'''
核心做法 我们最多能分多少段 n段 应该是 message的长度
<a1/b1> 每一个tail的长度 如何计算
1 suma1 = sum(len(1)---len(i))  i means how many part
2 sumb1 = len(parts) * part  how many parts , limit
3 </> fix 3 for each part

judge condition
limit * parts == final length
final length - (suma + sumb + sumc) == really string size
if that is bigger than message length, means we a valid part

'''
from typing import List


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        maxparts, suma = len(message), 0

        for parts in range(1, maxparts + 1):
            suma += len(str(parts))
            sumb, sumc = len(str(parts)) * parts, 3 * parts
            if limit * parts - (suma + sumb + sumc) >= len(message):
                ret, p = [], 0
                for i in range(1, parts + 1):
                    tail = "<%d/%d>" % (i, parts)
                    ret.append(message[p:p + limit - len(tail)] + tail)
                    p += limit - len(tail)
                return ret

        return []


    def splitMessagePrac(self, message: str, limit: int) -> List[str]:
        '''
        we can define a maxPart.--> max Value is length of message
        which means maximal parts we can split.
        in each part
        <a/b>---> can be form as length of a , length of b length of </>
        totalLength of a = sum(1 + 2 + .... parts)
        totallength of b = maxParts * length(parts)
        totallength of c = 3 * maxParts

        limits * parts - sumA - sumB - sumC = valid message length
        we need this length >= len(message)
        '''
        max_parts = len(message)
        sum_a = 0
        for part in range(1,max_parts):
            sum_a += len(part)
            sum_b = max_parts * len(part)
            sum_c = max_parts * 3
            if limit * part - (sum_a + sum_b + sum_c) > len(message): ## we can get all message form the string
                res = []
                pointer = 0
                for i in range(1,part + 1):
                    tail = "<%d/%d>"%(i,part)
                    res.append(message[pointer:pointer + limit - len(tail)] + tail)
                    pointer += limit - len(tail)

                return res
        return []