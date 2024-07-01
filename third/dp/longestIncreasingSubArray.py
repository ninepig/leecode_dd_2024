# https://www.geeksforgeeks.org/longest-increasing-subarray/

def lenOfLongIncSubArr(arr, n):
    # 'max' to store the length of longest
    # increasing subarray
    # 'len' to store the lengths of longest
    # increasing subarray at different
    # instants of time
    m = 1
    l = 1

    # traverse the array from the 2nd element
    for i in range(1, n):

        # if current element if greater than previous
        # element, then this element helps in building
        # up the previous increasing subarray encountered
        # so far
        if (arr[i] > arr[i - 1]):
            l = l + 1
        else:

            # check if 'max' length is less than the length
            # of the current increasing subarray. If true,
            # then update 'max'
            if (m < l):
                m = l

                # reset 'len' to 1 as from this element
            # again the length of the new increasing
            # subarray is being calculated
            l = 1

    # comparing the length of the last
    # increasing subarray with 'max'
    if (m < l):
        m = l

    # required maximum length
    return m


# Driver program to test above

arr = [5, 6, 3, 5, 7, 8, 9, 1, 2]
n = len(arr)
print("Length = ", lenOfLongIncSubArr(arr, n))


def printLongestIncSubArr(arr, n):
    # 'max' to store the length of longest
    # increasing subarray
    # 'len' to store the lengths of longest
    # increasing subarray at different
    # instants of time
    m = 1
    l = 1
    maxIndex = 0

    # traverse the array from the 2nd element
    for i in range(1, n):

        # if current element if greater than previous
        # element, then this element helps in building
        # up the previous increasing subarray
        # encountered so far
        if (arr[i] > arr[i - 1]):
            l = l + 1
        else:

            # check if 'max' length is less than the length
            # of the current increasing subarray. If true,
            # then update 'max'
            if (m < l):
                m = l

                # index assign the starting index of
                # longest increasing contiguous subarray.
                maxIndex = i - m

            # reset 'len' to 1 as from this element
            # again the length of the new increasing
            # subarray is being calculated
            l = 1

            # comparing the length of the last
    # increasing subarray with 'max'
    if (m < l):
        m = l
        maxIndex = n - m

    # Print the elements of longest
    # increasing contiguous subarray.
    for i in range(maxIndex, (m + maxIndex)):
        print(arr[i], end=" ")


# Driver program to test above
arr = [5, 6, 3, 5, 7, 8, 9, 1, 2]
n = len(arr)
printLongestIncSubArr(arr, n)
