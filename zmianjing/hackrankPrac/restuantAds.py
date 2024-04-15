import collections


class Solution:

    def leastDayToGiveAds(self, restaurants, duration):
        ##santity check
        if not restaurants or len(restaurants) == 0:
            raise Exception("Wrong input")
        '''
        Axxxxx   5 x means freezing duration
        AXXXXX    if we have 6 A -- which means max = 6
        AXXXXX    then we need find how many item has 6 ads. if so , we can fill them into x slot
        Axxxxx    IF WE HAVE 6 B 6 C , WE CAN FILL IN THEM .
        Axxxxx    ALL THE OTHER ITEM CAN BE FILL IN X
        ABC
        so considering freetime , at least we need this much days to finish that
        '''
        res_counter = collections.Counter(restaurants)
        max_ads = max(res_counter.values())
        count_max_ads = 0
        for v in res_counter.values():
            if v == max_ads:
                count_max_ads += 1

        return max(len(restaurants), (max_ads - 1) * (duration + 1) + count_max_ads)

    def leastDayToGiveAdsInorder(self, restaurants, duration):
        ## santity check
        ## ..
        res = 0
        last_finished = dict()
        for item in restaurants:
            res += 1
            if item in last_finished:
                ## the early's day we can do this ad if that was seen last time , +1 means we need one day to finish that
                res = max(res, last_finished[item] + 1 + duration)
            last_finished[item] = res

        return res


