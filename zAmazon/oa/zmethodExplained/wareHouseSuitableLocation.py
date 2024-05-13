#https://www.fastprep.io/problems/amazon-number-of-suitable-locations
import math


def isValid(center, d, location):
    res = 0
    for item in center:
        res += 2 * abs(location - item)
        if res > d:
            return False
    return True

def lowerBound(center, d, left, right):
    while left + 1 < right:
        mid = left + (right - left) // 2
        # print(left,right)
        # print(mid)
        if isValid(center,d,mid):
            right = mid;
        else:
            left = mid
    if isValid(center,d,left):
        return left
    if isValid(center,d,right):
        return right
    return -1


def higherBound(center, d, left, right):
    while left + 1 < right:
        mid = left + (right - left) // 2
        if isValid(center, d, mid):
            left = mid;
        else:
            right = mid
    if isValid(center, d, left):
        return left
    if isValid(center, d, right):
        return right
    return -1


def getLocations(center,d):
    if not center or len(center) == 0:
        return 0
    maxLoc = -math.inf
    minLoc = math.inf
    numberOfCenter = len(center)

    sum = 0
    for item in center:
        sum += item
        maxLoc = max(maxLoc,item)
        minLoc = min(minLoc,item)

    midPoint = sum//numberOfCenter
    left = minLoc - d
    right = maxLoc + d
    # print(midPoint)
    # print(left)
    # print(right)
    minValid = lowerBound(center,d,left,midPoint)
    maxValid = higherBound(center,d,midPoint,right)

    if minValid == -1 and maxValid == -1:
        return 0

    return maxValid - minValid + 1


# center = [-2,1,0]
# d = 8

center = [-3, 2, 2]

d = 8

print(getLocations(center,d))