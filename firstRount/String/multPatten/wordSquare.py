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

    def search(self, word: str):
        """
        Returns if the word is in the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                return []
            cur = cur.children[ch]

        res = []
        self.dfs(word,res)
        return res

    # 返回前缀为word的所有单词， 经典
    def dfs(self, word, res):
        cur = self
        if cur.isEnd :
            res.append(word)
        for ch in cur.children:
            node = cur.children[ch]
            node.dfs(word + ch , res)

'''
trie + dfs 回溯法 太经典了 细细品味'''
class Solution:

    def backtrace(self, index, size, path, res, trie_tree):
        if index == size:
            res.append(path[:])
        '''
        b a l l
        a r e a
        l e a d
        l a d y
        比如第一个单词是 ball，那么单词方块的长度是 4 * 4，则下一个单词（第二个单词）的前缀为 a。这样我们就又找到了一个以 a 为前缀且长度为 4 的单词，
        即 area，此时就变成了 [ball, area]。
            那么下一个单词（第三个单词）的前缀为 le。
            这样我们就又找到了一个以 le 为前缀且长度为 4 的单词，即 lead。此时就变成了 [ball, area, lead]。
            最后一个的前缀是lad 因为前三个单词已经固定了
            从代码上而言 就是每一个确定单词的第index位 ， 比如已经有三个词确定了。 那第四个词的开始 就必须是 LAD, word[i][index]'''
        next_prefix = ""
        for i in range(index):
            next_prefix += path[i][index]

        next_words_with_prefix = trie_tree.search(next_prefix)
        for word in next_words_with_prefix:
            path.append(word)
            self.backtrace(index + 1, size, path, res, trie_tree)
            path.pop(-1)

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie_tree = Trie()
        for word in words:
            trie_tree.insert(word)

        size = len(words[0])
        res = []
        path = []
        for word in words:
            path.append(word)
            self.backtrace(1,size,path,res,trie_tree)
            path.pop(-1)

        return res