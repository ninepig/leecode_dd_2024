from typing import List


class Trie:
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        self.word = ""

    def insert(self, word : str):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True
        cur.word = word


    def search(self, word : str) -> bool:
        cur = self
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return  cur is not None and cur.isEnd

class Solution:
    '''dfs + trie 学习下python 内部函数的用法'''
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_tree = Trie()
        for word in words:
            trie_tree.insert(word)
        # 4 direct
        directs = [(0,1),(0,-1),(1,0),(-1,0)]
        row = len(board)
        col = len(board[0])
        ans = set()
        #基本的dfs 玩法
        def dfs(cur, row, col):
            ch = board[row][col]
            if ch not in cur.children:
                return

            cur = cur.children[ch]
            if cur.isEnd:
                ans.add(cur.word)

            board[row][col] = "#"
            for direct in directs:
                newRow = row + direct[0]
                newCol = col + direct[1]
                if 0 <= newRow < row and 0 <= newCol < col:
                    dfs(cur,newRow,newCol)

            board[row][col] = ch

        for i in range(row):
            for j in range(col):
                dfs(trie_tree,i,j)

        return list(ans)