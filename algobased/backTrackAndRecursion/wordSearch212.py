class TrieTree:
    def __init__(self):
        self.children = dict()
        self.word = False

    def insert(self,word):
        cur = self
        for char in word:
            if char not in cur.children:
                # 这才对嘛。。
                cur.children[char] = TrieTree()
            cur = cur.children[char]
        cur.word = True

    def search(self,word):
        cur = self
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        return cur is not None and cur.word


def dfs(row, col, path, board, trie_helper, res):
    if trie_helper.word:
        res.append(path)
        trie_helper.word = False # missed this step

    if row < 0 or row >= len(board) or col < 0 or col>= len(board[0]):
        return
    cur_char = board[row][col]
    if not trie_helper.children[cur_char]:
        return
    # work as a visited flag
    board[row][col] = "#"
    dfs(row + 1 , col , path + cur_char , board , trie_helper.children[cur_char],res)
    dfs(row  , col + 1 , path + cur_char , board , trie_helper.children[cur_char],res)
    dfs(row  , col - 1 , path + cur_char , board , trie_helper.children[cur_char],res)
    dfs(row - 1 , col , path + cur_char , board , trie_helper.children[cur_char],res)
    board[row][col] = cur_char


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words:
            return []
        res = []
        trie_helper = TrieTree()
        length = len(board)
        width = len(board[0])
        for word in words:
            trie_helper.insert(word)

        for row in range(length):
            for col in range(width):
                dfs(row,col,"",board,trie_helper,res)

        return res


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


class SolutionAnswer(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp