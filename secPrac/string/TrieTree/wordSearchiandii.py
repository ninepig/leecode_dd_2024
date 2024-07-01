class Solution:
    # 第一题就是back tracking
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        length = len(board)
        width = len(board[0])
        visited = [[False for _ in range(length)] for _ in range(width)]

        def dfs(i,j,index):
            if index == len(word) - 1:
                return board[i][j] == word[index] # length same, compare last char

            if board[i][j] == word[index]:
                visited[i][j] = True
                for direct in directions:
                    new_i = i + direct[0]
                    new_j = j + direct[1]
                    if 0 <= new_i < length and 0 <= new_j < width and visited[new_i][new_j] == False:
                        if dfs(new_i,new_j,index + 1):
                            return True
                visited[i][j] = False

            return False

        for i in range(length):
            for j in range(width):
               if dfs(i,j,0):
                   return True

        return False

class Trie:
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        self.word = ""

    def insert(self,word:str):
        cur = self
        for ch in cur.children:
            if not cur.children[ch]:
                cur.children[ch] = Trie()
            cur = cur.children[ch]

        cur.isEnd = True
        # 把word记录下来 避免path的使用
        cur.word = word

    def search(self,word:str):
        cur = self
        for ch in cur.children:
            if not cur.children[ch]:
                return False
            cur = cur.children[ch]

        return cur is not None and cur.isEnd


class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        TrieHelper = Trie()
        for word in words:
            TrieHelper.insert(word)

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        board_row = len(board)
        board_col = len(board[0])
        ans = []

        def dfs(row,col,cur):
            ch = board[row][col]
            if ch not in cur.children:
                return

            cur = cur.children[ch]
            if cur.isEnd:
                ans.append(cur.word)

            board[row][col] = "#" # mark as visited
            for direct in directions:
                new_row = row + direct[0]
                new_col = col + direct[1]
                if 0<=new_row < board_row and 0 <= new_col < board_col:
                    dfs(new_row,new_col,cur)

            board[row][col] = ch #mark back for backtracking

        for i in range(board_row):
            for j in range(board_col):
                dfs(i,j,TrieHelper)

        return list(set(ans)) # remove duplcated