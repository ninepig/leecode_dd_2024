from typing import List

'''
python 语法
 for entry in d.items(): 对于map 里的entry
 entry[0] 代表的是key entry[1] 代表的是value
'''

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """
              :type matrix: List[List[int]]
              :rtype: List[int]
              """
        d = {}
        # loop through matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # if no entry in dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i + j] = [matrix[i][j]]
                else:
                    # If you've already passed over this diagonal, keep adding elements to it!
                    d[i + j].append(matrix[i][j])
            # we're done with the pass, let's build our answer array
        ans = []
        #print(d.items())
        # look at the diagonal and each diagonal's elements
        for entry in d.items():
            # each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
            # snake time, look at the diagonal level
            #print(entry[0])
            if entry[0] % 2 == 0:
                # Here we append in reverse order because its an even numbered level/diagonal.
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans

    def findDiagonalOrderSec(self, matrix: List[List[int]]) -> List[int]:
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        dict = {}
        for idxi in range(len(matrix)):
            for idxj in range(len(matrix[0])):
                if idxj + idxj not  in dict:
                    dict[idxi+idxj] = [matrix[idxi][idxj]]
                else:
                    dict[idxi+idxj].append(matrix[idxi][idxj])
        ans = []
        for entry in dict.items:
            if entry[0] % 2 == 0:
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1][::]]

        return  ans


sol = Solution()
maxtrix = [[1,2,3],[4,5,6],[7,8,9]]

print(sol.findDiagonalOrder(maxtrix))