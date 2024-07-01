import collections
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        counter_s = collections.Counter(s)
        sorted_counter = sorted(counter_s.items(),key= lambda item:item[1],reverse=True)
        # print(sorted_counter)
        res = []
        for item in sorted_counter:
            count = item[1]
            while count > 0:
                res.append(item[0])
                count -= 1

        return ''.join(res)

    def frequencySortHeap(self, s: str) -> str:
        # 统计元素频数
        s_dict = dict()
        for ch in s:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1

        priority_queue = []
        for ch in s_dict:
            heapq.heappush(priority_queue, (-s_dict[ch], ch))

        res = []
        while priority_queue:
            ch = heapq.heappop(priority_queue)[-1]
            times = s_dict[ch]
            while times:
                res.append(ch)
                times -= 1
        return ''.join(res)


test ="abccccd"
counter_s = collections.Counter(test)
sorted_counter = sorted(counter_s.items(), key=lambda item: item[1], reverse=True)
res = []
for item in sorted_counter:
    res.append(item[0])
print(res)