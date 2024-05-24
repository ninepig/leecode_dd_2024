'''
sure trust and safety group

'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        ## 这道题是个贪心题
        ## 因为只能换一次 所以需要把最左边的数 换到最右边最大的值
        num = [int(i) for i in str(num)]
        for i in range(len(num) - 1):
            m = max(num[i+1:])
            if num[i] < m:
                ## 从后往前找，右侧最大的，找到了 就交换
                for j in range(len(num) - 1, i , -1):
                    if num[j] == m:
                        break
                    num[i],num[j] = num[j],num[i]
                    break
        return int("".join([str(i) for i in num]))
