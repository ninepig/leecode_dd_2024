class Solution:


    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # Sort the array in non-increasing order
        n = len(citations)
        h = 0

        # Iterate through the sorted array and compare each citation count to the number of papers
        # that have at least that many citations
        for i in range(n):
            if citations[i] >= i + 1:
                # If the citation count is greater than or equal to the number of papers
                # with at least that many citations, we have found the h-index
                h = i + 1

        return h

'''

Frequency Array: Creates a temporary array temp of size n + 1 to store citation frequencies.
Counting Citations: Iterates through the citations list:
If a citation v is greater than n, adds it to the highest frequency bucket (temp[n]).
Otherwise, increments the count in the corresponding bucket (temp[v]).
Calculating h-index: Iterates backward through the temp array:
Accumulates the total number of citations up to each index i.
If the total count (total) is greater than or equal to i itself, it means i is the h-index.
Returns i as the h-index.
'''
class SolutionBucket:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        temp = [0 for _ in range(n + 1)]

        for i, v in enumerate(citations):
            if v > n:
                temp[n] += 1
            else:
                temp[v] += 1

        total = 0
        for i in range(n, -1, -1):
            total += temp[i]
            if total >= i:
                return i