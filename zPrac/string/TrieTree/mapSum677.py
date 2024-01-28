
'''dfs + trie 非常好的题'''

class TrieTree:
    def __init__(self):
        self.childend = dict()
        self.isEnd = False
        self.value = 0

    def insert(self,word:str,value:int):
        cur = self
        for ch in word:
            if not self.childend[ch]:
                self.childend[ch] = TrieTree()
            cur = self.childend[ch]
        cur.isEnd = True
        cur.value =value

    def search(self,word:str)->int:
        cur = self
        for ch in word:
            if not self.childend[ch]:
                return 0
            cur = self.childend[ch]
        return self.dfs(cur)

    def dfs(self,cur)->int:
        if not cur:
            return 0
        res = cur.value
        for node in cur.childend.values(): # 这个value 不是值,而是children dict里value的所有item, 也就是它存在children所有的值都要dfs下
            res += self.dfs(node)

        return res



class MapSum:

    def __init__(self):
        self.trieTree= TrieTree()

    def insert(self, key: str, val: int) -> None:
        self.trieTree.insert(str,val)

    def sum(self, prefix: str) -> int:
        return self.trieTree.search(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)