# https://www.fastprep.io/problems/amazon-calculate-median-sum
'''
You are given a list of packets of varying sizes and there are n channels.

Each of the n channel must have a single packet
Each packet can only be on a single channel
The quality of a channel is described as the median of the packet sizes on that channel.
The total quality is defined as sum of the quality of all channels (round to integer in case of float).

Given the packet sizes and num of channels, find the maximum quality.
'''
from typing import List
import math

## 这个题比较直观

def medianOf(nums:List[int])->int:
    n = len(nums)
    m = int(n/2)
    if n % 2 == 0: ##  1 2 3 4 5 6
        return math.ceil((nums[m-1] + nums[m]) / 2)
    else: ##  1 2 3 4 5
        return (nums[(int((n-1)/2))])



def calculateMedianSum(packets:List[int], n:int) -> int:
    if n > len(packets):return -1
    if n == 0: return -1

    packet_bucket = [] # [5], [1234]

    packets.sort()

    while n > 0:
        if n > 1:
            biggest_item = packets.pop()
            packet_bucket.append([biggest_item])
        else:
            packet_bucket.append(packets)
        n -= 1


    sum_of_qualities = 0
    for p in packet_bucket:
        sum_of_qualities += medianOf(p)

    return sum_of_qualities

# packets = [5, 2, 2, 1, 5, 3]
# n = 2
packets = [1, 2, 3, 4, 5]
n = 2

print(calculateMedianSum(packets, n))