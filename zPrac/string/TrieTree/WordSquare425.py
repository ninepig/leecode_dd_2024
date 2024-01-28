class TrieTree:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

    def insert(self,word:str):
        cur = self
        for ch in word:
            if not cur.children[ch]:
                cur.children[ch] = TrieTree()
            cur = cur.children[ch]

        cur.isEnd = True

    def search(self,word:str):
        cur = self
        for ch in word:
            if not cur.children[ch]:
                return []
            cur = cur.children[ch]

        res = []
        cur.dfs(word,res)
        return res

    def dfs(self,word,res):
        cur = self
        if cur and cur.isEnd:
            res.append(word)
            return
        for ch in cur.children:
            node = cur.children[ch]
            node.dfs(word + ch ,res)

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie_helper = TrieTree()
        for word in  words:
            trie_helper.insert(word)

        path = []
        res = []
        size = words[0]

        for word in words:
            path.append(word)
            self.backtrack(1,size,path,res,trie_helper)
            path.pop(-1)

        return res

    def backtrack(self, index, size, path, res, trie_helper):
        if index == size:
            res.append(path[:])
        next_prefix = ""
        for i in range(index): ## 下一行的前缀
            next_prefix += path[i][index]

        next_words_with_prefix = trie_helper.search(next_prefix)
        for word in next_words_with_prefix:
            path.append(word)
            self.backtrack(index + 1, size,path,res,trie_helper)
            path.append(-1)