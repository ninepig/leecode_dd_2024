class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        dirs= [(-1,0),(1,0),(0,1),(0,-1)]
        rows = len(board)
        cols = len(board[0])
        def dfs(row,col,index):
            if index == len(word):
                ## reach end of word
                return True

            if not (0 <= row < rows and 0<= col < cols):
                return False ## out of board

            if word[index] != board[row][col]:
                return False # not right word

            temp = board[row][col]
            board[row][col] = "" ## set visited
            found = False
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                found |= dfs(new_row,new_col,index + 1) ## any direction found target is fine.
            board[row][col] = temp #back track
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True

        return False

import  collections
class SolutionBFS:
	def exist(self, board: list[list[str]], word: str) -> bool:
		n, m = len(board), len(board[0])
		adj = [(0,-1), (0,1), (1,0), (-1,0)]

		graph = collections.defaultdict(list)
		letters = set()
		for i in range(n):
			for j in range(m):
				letters.add(board[i][j])
				for l, k in adj:
					if 0 <= i + l < n and 0 <= j + k < m:
						graph[(i,j)].append((i+l,j+k))

		for i in word:
			if i not in letters: return False

		def bfs(i,j):
			w = board[i][j]
			p = set()
			p.add((i,j))
			Q = collections.deque([(w, i, j, 0, p)])
			while Q:
				current, r, c, level, path = Q.popleft()
				if current == word: return True
				for l, k in graph[(r,c)]:
					if board[l][k] == word[level+1]:
						if (l,k) in path: continue
						p = path.copy()
						p.add((l,k))
						Q.append( (current+board[l][k], l, k, level + 1, p) )
			return False

		for i in range(n):
			for j in range(m):
				if word[0] == board[i][j]:
					x = bfs(i,j)
					if x: return x
		return False

class Solution2:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
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