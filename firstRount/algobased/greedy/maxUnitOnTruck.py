class Solution:
    '''贪心,如何尽量装的多,排序从大到小,先赛大的 再小的'''
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x:x[1],reverse=True) # 从大到小排列unit大小
        res = 0
        help_szie = truckSize
        for box in boxTypes:
            if help_szie > box[0]:
                help_szie -= box[0]
                res += box[1] * box[0]
            else: # once it can not fill, it means this is could be last load, part load, load part of current box
                res += box[1] * help_szie
                break # end loading

        return res

