class TrieTree:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

    def insert(self,word:str):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieTree()
            cur = cur.children[ch]
        self.isEnd = True

    def search(self,word:str):
        cur = self
        for ch in word:
            if ch.islower():
                if ch not in cur.children:
                    continue
            else:
                if ch not in cur.children:
                    return False
            cur = cur.children[ch]

        return cur is not None and cur.isEnd == True



class Solution:
    '''trie search的时候只看大写的字符是否存在 小写直接跳过
    大写 如果存在 继续, 不存在 返回false'''
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        trie_helper = TrieTree()
        trie_helper.insert(pattern)
        ans = []
        for query in queries:
            ans.append(trie_helper.search(query))

        return ans
    