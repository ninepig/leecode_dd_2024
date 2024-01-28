import heapq


class Solution:
    '''最大堆, 因为我们从顶部pop出来的元素就是最大的frenqucy的元素'''
    def frequencySort(self, s: str) -> str:
        pq = []
        res = []
        count_dict = dict()
        for c in s:
            if c not in count_dict:
                count_dict[c] = 1
            else:
                count_dict[c] += 1

        for item,frequent in count_dict.items():
            heapq.heappush(pq,(-frequent,item)) # we want max heap

        while heapq:
            # cur_fre,cur_item = -pq[0][0],pq[0][1] # heap不能这么看 ,heap的第一个不一定是顶部节点
            # heapq.heappop()
            cur_item = heapq.heappop(pq)[-1]
            cur_fre = count_dict[cur_item]
            while cur_fre :
                res.append(cur_item)
                cur_fre -= 1

        return "".join(res)



