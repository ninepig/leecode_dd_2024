class TrieTree:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

    def insert(self,word:str):
        root = self
        for ch in word:
            if not self.children[ch]:
                self.children[ch] = TrieTree()
            root = self.children[ch]
        root.isEnd = True

    def search(self,word:str):
        root = self
        for ch in word:
            if not self.children[ch]:
                return False
            root = self.children[ch]
        return root and root.isEnd


class Solution:
    '''
    dictionay is list of root
    sentence is a word string using space to split
    replace sentence's word with shortest root

    自己的方法不好, 可以直接在trie上搜索 words,利用一个index来做
    '''
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        Trie = TrieTree()
        for item in dictionary:
            Trie.insert(item)
        ans = []
        word_list = sentence.split(" ")
        for word in word_list:
            for i in len(word):
                temp = word[:i]
                if Trie.search(temp):
                    ans.append(temp)
                    break
                if temp == word and not Trie.search(word):
                    ans.append(temp)

        return " ".join(ans)


## better solution
## 在search之中处理逻辑 满分!
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True


    def search(self, word: str) -> str:
        """
        Returns if the word is in the trie.
        """
        cur = self
        index = 0
        for ch in word:
            if ch not in cur.children:
                return word
            cur = cur.children[ch]
            index += 1
            if cur.isEnd:
                break
        return word[:index]


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie_tree = Trie()
        for word in dictionary:
            trie_tree.insert(word)

        words = sentence.split(" ")
        size = len(words)
        for i in range(size):
            word = words[i]
            words[i] = trie_tree.search(word)
        return ' '.join(words)