# https://www.fastprep.io/problems/amazon-review-score



'''
Case 5:
Fail (Hidden Testcase)
your output: 1
expected output: 0
inputs:
fruits = [10, 10, 10, 11, 11, 11, 12, 12, 12]

Case 14:
Fail (Hidden Testcase)
your output: 0
expected output: 2
inputs:
fruits = [46, 46, 47, 47, 48, 48, 49, 49, 50, 50, 51, 51, 52, 52]

极端情况 
这两种是错的 

https://www.1point3acres.com/bbs/thread-1037532-1-1.html
正确答案
'''
from typing import List
import collections
import heapq
# fruits = [3, 3, 1, 1, 2]
# fruits = [1, 2, 5, 6]
# fruits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
#           5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
#           6, 6, 6, 6,
#           7, 7]
# fruits = [46, 46, 47, 47, 48, 48, 49, 49, 50, 50, 51, 51, 52, 52]
fruits = [10, 10, 10, 11, 11, 11, 12, 12, 12] ## if we have same value, that should do some other handling

def getMinimumFruits(fruits: List[int]) -> int:
    # We only need to check frequencies, fruits themselves are not needed
    # We willuse a max heap, to get max 2 freq, crush them and put back, then do the same again until heap lenght <= 1
    freqOfFruits = [(freq * -1) for freq in list((collections.Counter(fruits)).values())]
    heapq.heapify(freqOfFruits)

    while len(freqOfFruits) > 1:
        # Get the most frequest 2 fruits
        first = heapq.heappop(freqOfFruits) * -1
        second = heapq.heappop(freqOfFruits) * -1

        # crush them
        remaining = abs(first - second)
        if remaining > 0:
            heapq.heappush(freqOfFruits, -1 * remaining)
        print(first, second, remaining, freqOfFruits)

    if len(freqOfFruits) == 0:
        return 0
    if len(freqOfFruits) == 1:
        return freqOfFruits[0] * -1
    else:
        return abs(freqOfFruits[0] - freqOfFruits[1])


def solve(fruits):
    count = collections.Counter(fruits)
    pq = [-freq for freq in count.values()]
    heapq.heapify(pq)
    while len(pq) > 1:
        freq1 = -heapq.heappop(pq)
        freq2 = -heapq.heappop(pq)
    # Decrement the frequencies and push back if more than 0
    if freq1 - 1 > 0:
        heapq.heappush(pq, -(freq1 - 1))
    if freq2 - 1 > 0:
        heapq.heappush(pq, -(freq2 - 1))
    return -pq[0] if pq else 0


print(getMinimumFruits(fruits))