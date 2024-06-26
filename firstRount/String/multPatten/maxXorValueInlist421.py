
'''非常经典的位运算题
复习了位运算的基本知识
位运算是只看位的加法
同时异或符合交换律
a^b = max ---> a^max = b
同时利用字典树
如果面经没有 就不考虑了. 非常牛逼的题

'''

class TrieNode:
    def __init__(self):
        self.children = dict()  # children nodes
        self.val = 0  # end value

class Trie:
    def __init__(self, n):
        self.root = TrieNode()  # root node
        self.n = n  # max length of all numbers

    def add_num(self, num):
        node = self.root
        for shift in range(self.n, -1, -1):  # only shift self.n bits
            val = 1 if num & (1 << shift) else 0  # verify bit from left to right
            if val not in node.children:
                node.children[val] = TrieNode()
            node = node.children[val]
        node.val = num

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_len = len(bin(max(nums))) - 2  # get max length of all numbers' binary
        trie = Trie(max_len)
        for num in nums: trie.add_num(num)  # build trie

        ans = 0
        for num in nums:  # for each num, find the number which can create max value with num using XOR
            node = trie.root
            for shift in range(max_len, -1, -1):
                val = 1 if num & (1 << shift) else 0  # verify bit from left to right
                node = node.children[1 - val] if 1 - val in node.children else node.children[
                    val]  # try opposite bit first, otherwise use same bit
            ans = max(ans, num ^ node.val)  # maintain maximum
        return ans


