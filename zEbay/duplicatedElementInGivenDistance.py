import collections


class solution:
    ## Write a function to determine whether duplicate elements in a given array are within a given distance of each other
    def checkDuplicated(self,nums:list[int],dis:int):
        '''
        hashmap -->value to indx , check if we see any elment with dis
        '''
        if not nums or len(nums) == 0: return False
        help_dict = dict()
        for i, v in enumerate(nums):
            if v not in help_dict:
                help_dict[v] = i
            else:
                if abs(help_dict[v] - i) <= dis:
                    return True
                ## if bigger than distance, updated to latest index
                help_dict[v] = i

        return False ## if not exist , return false



