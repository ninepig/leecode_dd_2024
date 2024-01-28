'''
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".

标准的Trie search
只不过insert的key 全是pattern
search的时候忽略小写

'''

class Trie:

    def __init__(self):
        self.children = dict()
        self.isEnd = False

    def insert(self, word: str) -> None:
        cur = self
        for ch in word:
            if ch not in cur.children :
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self
        for ch in str:
            if ord(ch) > 96: # if ch is lower case
                continue
            else:
                if ch not in cur.children: # ch is not in trie , means does not match
                    return False
            cur = cur.children[ch]
        return cur is not None and cur.isEnd

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        tire_tree = Trie()
        tire_tree.insert(str)
        res = []
        for query in queries:
            res.append(tire_tree.search(query))

        return res