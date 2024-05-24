'''
描述：给定一个由许多词根组成的字典列表 dictionary，以及一个句子字符串 sentence。

要求：将句子中有词根的单词用词根替换掉。如果单词有很多词根，则用最短的词根替换掉他。最后输出替换之后的句子
输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"

字典树 ---> 创建词根树
词---> 找到词根 输出
'''

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = True

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isEnd = True

    def search(self, word:str) -> str:
        cur = self.root
        index = 0
        for ch in word:
            # search 一定要线检查如果不存在的情况
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