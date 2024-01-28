class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        res = []
        slots1.sort()
        slots2.sort()
        size1 = len(slots1)
        size2 = len(slots2)
        left1,left2 = 0,0
        while left1 < size1 and left2 < size2:
            slots1_cur = slots1[left1]
            slots2_cur = slots2[left2]
            start = max(slots1_cur[0],slots2_cur[1])
            end = max(slots1_cur[1],slots2_cur[1])
            if end - start > duration:
                return [start,start+duration]
            if slots2_cur[end] < slots1_cur[end]:
                left2 += 1
            else:
                left1 += 1

        return res