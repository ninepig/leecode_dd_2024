import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        # get freq
        fre_dict = []
        for ch in s:
            fre_dict[ch] = fre_dict.get(ch,0) + 1

        # sort by frency
        max_heap = []
        for key,fre in fre_dict:
            heapq.heappush(max_heap,(fre,key))

        # output
        res = []
        while max_heap:
            ch = heapq.heappop(max_heap)[-1]
            times = fre_dict[ch] # 或者是 push tuble， item[0] --> times
            while times:
                res.append(ch)
                times -= 1
        return ''.join(res)