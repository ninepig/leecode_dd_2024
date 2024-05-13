# https://www.fastprep.io/problems/amazon-find-kth-minimum-vulnerability

import heapq
from typing import List

'''
Amazon Web Services has n servers where the ith server's vulnerability score is vulnerability[i]. 
A client wants to deploy their application on a group of m contiguous servers. 
The vulnerability of a group is defined as the kth minimum vulnerability among the chosen servers. 
Find the vulnerability of each possible group of m contiguous servers the client can choose.

Function Description

Complete the function findKthMinimumVulnerability in the editor below.

findKthMinimumVulnerability has the following parameter(s):

int k: the order of the vulnerability to find
int m: the number of servers in a group
int vulnerability[n]: the vulnerabilities of each server
'''
class Solution:
    def findKthMinimumVulnerability(self, k: int, m: int, vulnerability: List[int]) -> List[int]:
        size = len(vulnerability)
        result = []
        for left in range(size):
            minHeap = []
            right = min(left + m, size)
            for i in range(left, right):
                heapq.heappush(minHeap, vulnerability[i])

            result.append(heapq.nsmallest(k, minHeap)[-1])

            if right == size:
                break

        return result

sol = Solution()
k = 3
m = 4
v = [4, 2, 3, 1, 1]
print(sol.findKthMinimumVulnerability(k,m,v))