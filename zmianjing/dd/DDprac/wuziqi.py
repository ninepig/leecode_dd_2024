n = 10
board = [[0] * n for _ in range(n)]
p1_x = [0, 0, 0, 0, 0]
p1_y = [1, 2, 3, 4, 5]
p2_x = [7, 3, 4, 7, 2]
p2_y = [3, 2, 3, 4, 2]


def search_line(a, b, x):
    # 1.行搜索
    count = 1
    flag1 = flag2 = 0
    for i in range(1, 5):
        if flag1 == 0 and b - i >= 0 and board[a][b - i] == x:
            count += 1
        else:
            flag1 = 1
        if flag2 == 0 and b + i < n and board[a][b + i] == x:
            count += 1
        else:
            flag2 = 1
    if count >= 5:
        return True
    else:
        return False


def search_column(a, b, x):
    # 2.列搜索
    count = 1
    flag1 = flag2 = 0
    for i in range(1, 5):
        if flag1 == 0 and a - i >= 0 and board[a - i][b] == x:
            count += 1
        else:
            flag1 = 1
        if flag2 == 0 and a + i < n and board[a + i][b] == x:
            count += 1
        else:
            flag2 = 1
    if count >= 5:
        return True
    else:
        return False


def search_left(a, b, x):
    # 3.左上到右下
    count = 1
    flag1 = flag2 = 0
    for i in range(1, 5):
        if flag1 == 0 and b - i >= 0 and a - i >= 0 and board[a - i][b - i] == x:
            count += 1
        else:
            flag1 = 1
        if flag2 == 0 and b + i < n and a + i < n and board[a + i][b + i] == x:
            count += 1
        else:
            flag2 = 1
    if count >= 5:
        return True
    else:
        return False


def search_right(a, b, x):
    # 4.右上到左下
    count = 1
    flag1 = flag2 = 0
    for i in range(1, 5):
        if flag1 == 0 and b + i < n and a - i >= 0 and board[a - i][b + i] == x:
            count += 1
        else:
            flag1 = 1
        if flag2 == 0 and b - i >= 0 and a + i < n and board[a + i][b - i] == x:
            count += 1
        else:
            flag2 = 1
    if count >= 5:
        return True
    else:
        return False


def search(a, b, x):
	# x：标志位 x为1时表示board棋盘的这个位置时p1;x为2时表示board棋盘的这个位置时p2
	# a,b为期盼的坐标
    board[a][b] = x

    return search_line(a, b, x) or search_column(a, b, x) or \
    search_left(a, b, x) or search_right(a, b, x)


for i in range(len(p1_x)):
    p1_win = search(p1_x[i], p1_y[i], 1)
    p2_win = search(p2_x[i], p2_y[i], 2)
    if p1_win:
        print(1)
    if p2_win:
        print(2)
    if not p1_win and not p2_win:
        print(0)



