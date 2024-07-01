class solution:
    ## default we use a 10 * 10 map
    def __init__(self):
        self.grid = [[0 for _ in range(10)] for _ in range(10)]

    def checkWhoWins(self, player_one_input: list[list[int]], player_two_input: list[list[int]]):
        if not player_one_input or not player_two_input:
            return 0

        ## need check if pos has duplcate problem for input ? todo
        for i in range(len(player_one_input)):
            ## 1 means play_one  2 means player_2
            p1_win = self.search(player_one_input[i], 1)
            p2_win = self.search(player_two_input[i], 2)
            if p1_win:
                return 1
            if p2_win:
                return 2
            if not p1_win and not p2_win:
                print("even")
        # no one win
        return 0

    def search(self, pos: list[int], player: int):
        if self.grid[pos[0]][pos[1]] != 0:
            print("invalid input")
            exit(0)
        self.grid[pos[0]][pos[1]] = player
        return (self.rowsCheck(pos[0], pos[1], player) or self.colsCheck(pos[0], pos[1], player)
                or self.dignalCheck(pos[0], pos[1], player) or self.antidignalCheck(pos[0], pos[1], player))

    def rowsCheck(self, a, b, x):
        # 1.行搜索
        count = 1
        # flag 1 2 代表左右有没有断 是否连成排
        flag1 = flag2 = 0
        for i in range(1, 10):
            if flag1 == 0 and b - i >= 0 and self.grid[a][b - i] == x:
                count += 1
            else:
                flag1 = 1
            if flag2 == 0 and b + i < 10 and self.grid[a][b + i] == x:
                count += 1
            else:
                flag2 = 1
            if count == 5:
                break
        if count >= 5:
            return True
        else:
            return False

    def colsCheck(self, a, b, x):
        # 2.列搜索
        count = 1
        flag1 = flag2 = 0
        for i in range(1, 10):
            if flag1 == 0 and a - i >= 0 and self.grid[a - i][b] == x:
                count += 1
            else:
                flag1 = 1
            if flag2 == 0 and a + i < 10 and self.grid[a + i][b] == x:
                count += 1
            else:
                flag2 = 1
            if count == 5:
                break
        if count >= 5:
            return True
        else:
            return False

    def dignalCheck(self, a, b, x):
        # 3.左上到右下
        count = 1
        flag1 = flag2 = 0
        for i in range(1, 10):
            if flag1 == 0 and b - i >= 0 and a - i >= 0 and self.grid[a - i][b - i] == x:
                count += 1
            else:
                flag1 = 1
            if flag2 == 0 and b + i < 10 and a + i < 10 and self.grid[a + i][b + i] == x:
                count += 1
            else:
                flag2 = 1
            if count == 5:
                break
        if count >= 5:
            return True
        else:
            return False

    def antidignalCheck(self, a, b, x):
        # 4.右上到左下
        count = 1
        flag1 = flag2 = 0
        for i in range(1, 10):
            if flag1 == 0 and b + i < 10 and a - i >= 0 and self.grid[a - i][b + i] == x:
                count += 1
            else:
                flag1 = 1
            if flag2 == 0 and b - i >= 0 and a + i < 10 and self.grid[a + i][b - i] == x:
                count += 1
            else:
                flag2 = 1
            if count == 5:
                break
        if count >= 5:
            return True
        else:
            return False


player_one_input = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
player_two_input = [[7, 3], [3, 2], [4, 3], [7, 4], [2, 2]]
sol = solution()
print(sol.checkWhoWins(player_one_input, player_two_input))