#https://www.fastprep.io/problems/amazon-get-min-num-moves
import math
from typing import List


def getMinNumMoves(blocks:List[int]) -> int:
    #Find indexes of min, max
    minn, maxx = (float('inf'), -1), (float('-inf'), -1)
    for i, n in enumerate(blocks):
        if n < minn[0]:
            minn = (n, i)
        if n > maxx[0]:
            maxx = (n, i)

    print("min, max", minn, maxx)

    # Moves needed to bring min to the beginning
    movesForMin = minn[-1]
    movesForMax = len(blocks)-maxx[-1]-1
    totalMoves = movesForMin + movesForMax

    # If max on the left of the min, it is also swapped a step while moving min, so deduce this step.
    if maxx[-1] < minn[-1]:
        totalMoves -= 1

    return totalMoves

print(getMinNumMoves([2, 4, 3, 1, 6]))
print(getMinNumMoves([4, 11, 9, 10, 12]))
print(getMinNumMoves([3, 2, 1]))