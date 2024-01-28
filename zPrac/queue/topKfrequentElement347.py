import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = dict()

        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        # remove duplicated in nums to do less cal
        new_num = list(set(nums))
        heap_array = []

        # maintain size k 's minHeap
        for num in new_num:
            heapq.heappush(heap_array,(num_dict[num],num))
            if len(heap_array) > k:
                heapq.heappop(heap_array)

        return [items[1] for items in heap_array]


