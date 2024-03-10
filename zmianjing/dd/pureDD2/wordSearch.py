'''
标准的dfs 题

要用bfs 有点难度
'''
from collections import defaultdict
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
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


'''bfs要构件图，所以比较复杂'''
class Solution2:
	def exist(self, board: List[List[str]], word: str) -> bool:
		n, m = len(board), len(board[0])
		adj = [(0,-1), (0,1), (1,0), (-1,0)]

		graph = defaultdict(list)
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
			Q = deque([( w, i, j, 0, p)])
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