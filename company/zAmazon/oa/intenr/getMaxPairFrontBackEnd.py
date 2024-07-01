# https://www.fastprep.io/problems/amazon-find-maximum-pairs

'''
An AWS client wants to deploy multiple applications and needs two servers,
one for their frontend and another for their backend. They have a list of integers representing the quality of servers in terms of availability. The client's preference is that the availability of an application's frontend server must be greater than that of its backend.

Two arrays of same size s, frontend[s] and backend[s] where elements represent the quality of servers,
create pairs of elements (frontend[i], backend[i]) such that frontend[i] > backend[i] in each pair. Each element from an array can be picked only once to form a pair. Find the maximum number of pairs that can be formed.

'''

class Solution:
  def findMaximumPairs(self, frontend: List[int], backend: List[int]) -> int:
    frontend.sort()
    backend.sort()

    f, b = len(frontend)-1 , len(frontend)-1
    res = 0
    while f >=0 and b >=0:
      if frontend[f] > backend[b]:
        res += 1
        f -= 1
        b -= 1
      else:
        b -= 1
    return res