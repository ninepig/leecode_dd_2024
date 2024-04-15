'''
'R......R' => 'RRRRRRRR'
'R......L' => 'RRRRLLLL' or 'RRRR.LLLL'
'L......R' => 'L......R'
'L......L' => 'LLLLLLLL'

四种

l指向区间的开始（指向 "L" 或者 "R"）；
r跳过所有的 "."，指向区间的结束（也指向 "L" 或者 "R"）。
此时区间的形状为 "X....Y"，判断这个区间左右端点的 "X"、 "Y"是什么，确定中间的 "."的状态。

	- you know the length of mid part
	- If char[i] == char[j] == 'R', means all go towards right (R)
	-  char[i]  == char[j] == 'L', means all go towards Left (L)
	-  If char[i] = 'L' and char[j] = 'R', means middle part is not affected so they remain '.'
	-  If char[i] = 'R' and char[j] = 'L', then it will affect the middle part.
	   The middle_part/2 close to i will be affected by 'R' and middle_part/2 close to j will be
	   effected by 'L'  and the last mid point (middle_part%2) will be unaffected due to equal
	   force from left and right so it remains '.'

'''

class Solution(object):
    def pushDominoes(self, d):
        """
        :type dominoes: str
        :rtype: str
        """
        d = "L" + d + "R" ## right r will not impact result
        res = []
        l = 0
        for r in range(1, len(d)):
            if d[r] == '.':
                continue
            mid = r - l - 1 ## l is 0 based so -1
            if l: # 虚拟的牌不放入结果
                res.append(d[l])
            if d[l] == d[r]:
                res.append(d[l] * mid)
            elif d[l] == 'L' and d[r] == 'R':
                res.append('.' * mid)
            else:
                res.append('R' * (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2))
            l = r
        return "".join(res)

