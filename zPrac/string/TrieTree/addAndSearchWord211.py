class TrieTree:
    def __init__(self):
        self.children =  dict()
        self.isEnd = False

    def insert(self,word:str):
        cur = self
        for ch in word:
            if not cur.children[ch]:
                cur.children[ch] = TrieTree()
            cur = cur.children[ch]
        cur.isEnd = True

    def search(self, word:str)->bool:
        def dfs(node,index):
            if index == len(word):
                return True

            ch = word[index]
            cur = node
            if ch == '.' :
                # 因为用了. 所以当前层所有的child 都可以满足条件,只需要判断child的下一层是否满足即可
                for child in cur.children.values(): # 用values
                    if child and dfs(child,index + 1):
                        return True
            else:
                if ch not in cur.children: # 不用values  因为要用到 key
                    return False
                child = cur.children[ch]
                if child and dfs(child,index + 1):
                    return True

            return False

        return dfs(self,0)


class WordDictionary:

    def __init__(self):
        self.Trie = TrieTree()

    def addWord(self, word: str) -> None:
        self.Trie.insert(word)

    # word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母
    def search(self, word: str) -> bool:
        return self.Trie.search(word)

