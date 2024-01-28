class Trie:
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
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return cur is not None and cur.isEnd == True



class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_tree = Trie()


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie_tree.insert(word)
    '''
    可以替换任意26个字母
    经典公式
    '''
    def search(self, searchWord: str) -> bool:
        if not searchWord or len(searchWord)<1:
            return False

        for i in range(len(searchWord)):
            for j in range(26):
                replace_char = chr(ord('a') + j)#关键词
                if replace_char != searchWord[i] : # if not same word
                    magic_word = searchWord[:i] + replace_char + searchWord[i+1:]
                    if self.trie_tree.search(magic_word):
                        return True

        return False



