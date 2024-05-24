import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre_dict = dict()
        for num in nums:
            # if num in fre_dict:
            #     fre_dict[num] += 1
            # else:
            #     fre_dict[num] = 1
            fre_dict[num] = fre_dict.get(num, 0) + 1

        heap = []
        for num, count in fre_dict.items():
            if len(heap) < k:
                heapq.heappush(heap,(count,nums))
            elif count > heap[0][0] :# 栈顶 frequency 是堆最小的，所以只要最小的比count 还要小，就要出栈
                heapq.heappop(heap)
                heapq.heappop(heap,(count,nums))

        res = []
        for item in heap:
            res.append(item[1])

        return res

        # return [num for count, num in heap]