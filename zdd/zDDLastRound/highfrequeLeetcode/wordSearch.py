import  collections

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        ##可以不用visit 用原grid + “.” 的方法  减少额外空间
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        def dfs(row,col,index):
            if index == len(word):
                return True
            if visited[row][col]:
                return False
            if board[row][col] == word[index]:
                visited[row][col] = True
                for dir in dirs:
                    new_row = row + dir[0]
                    new_col = col + dir[1]
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if dfs(new_row,new_col,index + 1):
                            return True
                visited[row][col] = False
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False

    def existBfs(self, board: list[list[str]], word: str) -> bool:
        # 处理边界情况
        if len(word) == 0 or not board or not board[0]:
            return False

        directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        len_word, board_row, board_column = len(word), len(board), len(board[0])

        queue = collections.deque()
        # 任意一个元素都有可能是入口, 将其入队
        for row in range(board_row):
            for column in range(board_column):
                if board[row][column] == word[0]:
                    queue.append(((row, column), 0,[]))

        while queue:
            index_board, index_word, visited_index = queue.popleft()
            # 如果board中的字符与word中的字符相同,则进行下一次比较, 否则不进行比较
            if board[index_board[0]][index_board[1]] == word[index_word]:
                # 如当前是word中的最后一个字符, 则说明前面的匹配成功
                if index_word == len_word - 1:
                    return True
                # 检查相邻的元素
                for direct in directs:
                    # 获取新的下标
                    new_row_index, new_column_index = index_board[0] + direct[0], index_board[1] + direct[1]
                    # 如果当前索引符合规范(没有越界, 没有被访问过)
                    if 0 <= new_row_index < board_row and 0 <= new_column_index < board_column and (new_row_index, new_column_index) not in visited_index:
                        queue.append(((new_row_index, new_column_index), index_word + 1, visited_index + [index_board]))
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