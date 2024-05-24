'''
贪心
太秒了
我们把这两种情况分别进行统计。

当遇到 s1[i] == s2[i] 时直接跳过。
当遇到 s1[i] == 'x'，s2[i] == 'y' 时，则统计数量到变量 xyCnt 中。
当遇到 s1[i] == 'y'，s2[i] == 'y' 时，则统计数量到变量 yxCnt 中。
则最后我们只需要判断 xyCnt 和 yxCnt 的个数即可。

如果 xyCnt + yxCnt 是奇数，则说明最终会有一个位置上的两个字符无法通过交换相匹配。
如果 xyCnt + yxCnt 是偶数，并且 xyCnt 为偶数，则 yxCnt 也为偶数。则优先交换 "xx" 与 "yy"、"yy" 与 "xx"。
即每两个 xyCnt 对应一次交换，每两个 yxCnt 对应交换一次，则结果为 xyCnt // 2 + yxCnt // 2。
如果 xyCnt + yxCnt 是偶数，并且 xyCnt 为奇数，则 yxCnt 也为奇数。则优先交换 "xx" 与 "yy"、"yy" 与 "xx"。
即每两个 xyCnt 对应一次交换，每两个 yxCnt 对应交换一次，则结果为 xyCnt // 2 + yxCnt // 2。最后还剩一组 "xy" 与 "yx" 或者 "yx" 与 "xy"，则再交换一次，则结果为 xyCnt // 2 + yxCnt // 2 + 2。

wenjing
如果是偶数 所有的转换都可以转换为 xx --> yy  yy-->xx  只需要做一次交换
如果是奇数 则说明一定会存在 xy-->yx的情况 就需要做两次交换
'''
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xycount,yxcount = 0,0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            elif s1[i] == 'x':
                xycount += 1
            else:
                yxcount += 1

        if (xycount + yxcount) % 2 ==1 :
            return False

        return xycount//2 + yxcount //2 + (xycount % 2 )*2