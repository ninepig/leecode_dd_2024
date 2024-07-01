#https://www.fastprep.io/problems/amazon-reverse-binary-string

'''
You are given a binary string. Find the minimum number of operations required to reverse it.
An operation is defined as: Remove a character from any index and append it to the end of the string.
Function Description
Complete the function reverseBinaryString in the editor.
'''
'''
双指针。。我没看懂
"00110101"
“10101100”
3

Ok I got it. You find the longest prefix of the reversed string that is also a subsequence of the original string.

My intuition is that after getting the longest prefix, you can manipulate the remaining operations 
such that the rest of the reversed string will be built. Answer will just be the n - len(longest prefix)

这个是正确的思路。 reverse以后。 找reversed是原数组最长的prefix 
java的解法是错的
'''
'''
    public int reverseBinaryString(String s) {
        // write your code here
        StringBuilder sb = new StringBuilder(s);
        String t = sb.reverse().toString();
        int l = 0;
        int r = 0;
        int res = 0;
        while (l < s.length()) {
            if (s.charAt(l) != t.charAt(r)) {
                l++;
                res++;
            } else {
                l++;
                r++;
            }
        }
        return res;
    }
    
}
'''
## 解法就是那么简单。。
def solve(s):
    n = len(s)
    rev = s[::-1]
    lp = 0
    for i in range(n):
        if s[i] == rev[lp]:
            lp += 1
    return n - lp

