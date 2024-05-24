import heapq


'''经典'''
class Solution:
    def frequencySort(self, s: str) -> str:
        count_table = []
        for c in s :
            if c in count_table:
                count_table[c] += 1
            else:
                count_table = 1

        # put in pq
        max_pq = []
        for key in count_table:
            heapq.heappush(max_pq,(-count_table[key],key))

        res = []
        # output with count
        while max_pq:
            cur_item = heapq.heappop(max_pq)
            count , ch = cur_item[0], cur_item[1]
            while count > 0:
                res.append(ch)
                count -= 1

        return ''.join(res)
