

'''
贪心
--->
三种情况
len(s)  < k --> false
len(s) = k --> true
lens(s) > k
1 if all char count in s is even ---> true
2 if some char count in s is odd ---> if count <= k ---> true


如果 len(s) > k，则需要判断一下字符串 s 中每个字符的个数。因为当字符是偶数个时，可以直接构造成回文串。
所以我们只需要考虑个数为奇数的字符即可。如果个位为奇数的字符种类小于等于 k，则说明可以构造 k 个回文串，返回 True。
如果个位为奇数的字符种类大于 k，则说明无法构造 k 个回文串，返回 Fasle。
'''
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        size =len(s)
        if size < k:
            return False
        if size == k :
            return True
        odd = 0
        char_counter = dict()
        for char in s:
            if char not in char_counter:
                char_counter[char] = 1
            else:
                char_counter[char] += 1
        for value in char_counter.values():
            if value % 2 == 1:
                odd +=1

        return odd <= k

