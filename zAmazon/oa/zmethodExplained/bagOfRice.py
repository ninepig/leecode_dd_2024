# https://www.fastprep.io/problems/max-set-size
## dfs handling this
from typing import List

'''
You are shopping on Amazon.com for some bags of rice. Each listing displays the number of grains of rice that the bag contains. You want to buy a perfect set of rice bags. From the entire search results list, riceBags. A perfect set of rice bags, perfect, is defined as:

The set contains at least two bags of rice.
When the rice bags in the set perfect are sorted in increasing order by grain count, it satisfies the condition perfect[i] * perfect[i] = perfect[i+1] for all 1 ≤ i < n. Here perfect[i] is the size of the set and perfect[i] is the number of rice grains in bag i.
Find the largest possible set perfect and return an integer, the size of that set. If no such set is possible, then return -1. It is guaranteed that all elements in riceBags are distinct.

Function Description

Complete the function maxSetSize in the editor.
'''

class Solution:
    def maxSetSize(self, riceBags: List[int]) -> int:
        riceBags.sort()
        maxSize = 0

        def backtracking(bags, perfectSet):
            nonlocal maxSize
            maxSize = max(maxSize, len(perfectSet))

            for i in range(len(bags)):
                bag = bags[i]
                if not perfectSet or perfectSet[-1] ** 2 == bag:
                    perfectSet.append(bag)
                    backtracking(bags[i + 1:], perfectSet)
                    perfectSet.pop()

        backtracking(riceBags, [])

        return maxSize if maxSize > 1 else -1


'''
hashset的方法比较好。。
public int findLargestSet(int[] onionBags) {
    // write your code here
  HashSet<Integer> set = new HashSet<>();
  for(int num : onionBags){
    set.add(num); 
  }

  int maxLength = 0;
  for(int num : onionBags){
    int temp = num;
    int len = 0;
    while(set.contains(temp)){
      temp = temp * temp;
      len += 1;
    }

    if(len > maxLength){
      maxLength = len;
    }
  }

  return maxLength;
  
}
'''