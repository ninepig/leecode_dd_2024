class Solution:
    '''这个题就是 统计出 1 的个数， 然后用这个个数来统计里windows里0的个数， 0最少 说明要交换的次数最少'''
    def minSwaps(self, data: List[int]) -> int:
        windows_size = 0
        for num in data:
            if num == 1:
                windows_size += 1
        windows_count = 0
        left =0
        right = 0
        res = float('inf')
        while right < len(data):
            if data[right] == 0:
                windows_count += 1
            if right - left + 1 >= windows_size:
               res = min(res,windows_count)
               if data[left] == 0:
                   windows_count -= 1
               left += 1
            right +=1

        return res if res != float('inf') else 0
    