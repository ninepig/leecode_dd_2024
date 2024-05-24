class solution:
    def uniqueRowOfMatrix(self,matrix:list[list[int]]):
        if not matrix or len(matrix) == 0:
            return []
        res = []
        row_set = set()
        for row in matrix:
            row_string = "".join(row)
            if row_string not in row_set:
                row_set.add(row_string)
                res.append(row)

        return res