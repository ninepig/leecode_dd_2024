'''
bfs

将1-9加入队列
取出一个元素，如果该元素长度为n，则继续执行2，否则执行3
在该元素的末尾添加一个新的数字，该数字是在末尾数字的基础上加k，-k，在合法的前提下，将当前数字加入队列，执行2

作者：hard何时不hard
链接：https://leetcode.cn/problems/numbers-with-same-consecutive-differences/solutions/612362/dui-lie-bfsqiu-jie-by-lzx1997-w6s7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''



def cal(s):
    res = 0
    for t in s:
        res = res * 10 + t
    return res


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        Q = collections.deque()
        for i in range(1, 10):
            Q.append([i])
        res = []
        while Q:
            v = Q.popleft()
            if len(v) == n:
                res.append(cal(v))
            elif k == 0:
                v.append(v[-1])
                Q.append(v)
            else:
                if v[-1] - k >= 0:
                    t = v.copy()
                    t.append(t[-1] - k)
                    Q.append(t)
                if v[-1] + k < 10:
                    t = v.copy()
                    t.append(t[-1] + k)
                    Q.append(t)
        return res
