class Solution:
    ## 数独 , 3组 dict 解决问题
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = [ dict() for _ in range(9)]
        col_dict = [dict() for _ in range(9)]
        box_dict = [dict() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                num = str(board[i][j])
                box_number = (i//3) * 3 + j//3 #小技巧
                row_count = row_dict[i].get(num,0)
                col_count = col_dict[j].get(num,0)
                box_count = box_dict[box_number].get(num,0)

                if row_count > 0 or col_count >0 or box_count > 0:
                    return False
                row_dict[i][num] = 1
                col_dict[j][num] = 1
                box_dict[box_number][num] = 1

        return True