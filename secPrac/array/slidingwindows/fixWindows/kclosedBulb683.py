class Solution:
    '''
    https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0683.%20K%20%E4%B8%AA%E5%85%B3%E9%97%AD%E7%9A%84%E7%81%AF%E6%B3%A1.md
    细细品味
    给定一个长度为 n 的灯泡数组 blubs，其中 bulls[i] = x 意味着在第i + 1 天，我们会把在位置 x 的灯泡打开，其中 i 从 0 开始，x 从 1 开始
    关键是转变在第几天哪个位置的bulb打开
    也就是day[pos]开灯时间'''
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        size = len(bulbs)
        pos_open_days = [0 for _ in range(size)]
        for i in range(size):
            ## day[pos] => openday
            pos_open_days[bulbs[i] - 1] = i + 1

        left= 0
        right = k + 1
        ans = float('inf')
        while right < size:
            good_flag = True
            for i in range(left + 1, right):
                # 比左右开灯都早， 就不满足， 必须中间的比左右都早开
                if pos_open_days[i] < pos_open_days[left] or pos_open_days[i]<pos_open_days[right]:
                    left,right = i , i + k + 1
                    good_flag = False
                    break
            if good_flag:
                ## 左右稍晚的哪个开灯时间 是答案， 再找最小的这个答案即可
                ans = min(ans,max(pos_open_days[left],pos_open_days[right]))

        return ans if ans != float('inf') else -1
