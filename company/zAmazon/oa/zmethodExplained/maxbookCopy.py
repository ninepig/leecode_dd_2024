# https://www.fastprep.io/problems/max-book-copies
from collections import Counter
from typing import List

'''
Amazon invests in the success of entrepreneurs, artisans, and small business selling in the Amazon Store. Some of these small business are book stores.

Amazon maintains a protal, where the booksellers can update their inventories. An update received from the portal is represented by the array portalUpdate, whose valuess indicate the following:

If portalUpdate[i] is a positive integer (for example 7), then a copy of the book with boook ID portalUpdate[i] is added to the inventory.
If portalUpdate[i] is a negative integer (for example -11), then a copy of the book with book ID portalUpdate[i] (i.e., book ID 11) is removed from the inventory. It is gauranteed that each such update will only be requested if the inventory currently has at least one copy of that book ID.
portalUpdate[i] is gauranteed to be non-zero.
Given the list of portal updates, the task is to return the maximum copies of any book in the inventory after each update.
'''
# 这个比较简单， 就是勇哥counter 来记数 。每次计算就行

class Solution:
    def maximumBookCopies(self, portalUpdate: List[int]) -> List[int]:
        updateDict = Counter()
        result = []

        for bookId in portalUpdate:
            if bookId > 0:
                updateDict[bookId] += 1
            else:
                updateDict[-bookId] -= 1
            result.append(max(updateDict.values()))

        return result

sol = Solution()
test = [1, 2, -1, 2]
print(sol.maximumBookCopies(test))

