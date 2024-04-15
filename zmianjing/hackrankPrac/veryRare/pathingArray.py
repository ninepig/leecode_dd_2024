class solution:
    '''
    s means missing number
    assumme we have every number  [0,s-1]  we can iterative visit x= num[i]
    so we can get [x, x+s-1] every number
    we sort nums ,
    if x <= missing, so we can get every number from [0, x+s-1]
    if x> missing, this means, we can not get missing. so we have to add some number to nums , using greedy
    we add missing number, which we can get maximum is [0,2s - 1]
    when missing number bigger than n, we get all number from [1,n]
    '''
    def patchArray(self,nums:list[int],N:int):
        if not nums or len(nums) == 0 : return 0
        missing = 1
        patch = 0
        idx = 0
        while missing <= N : # when missing number bigger than N, end loop, we find everything we need
            ## if we can find a number smaller than missing
            if idx < len(nums) and nums[idx] <= missing: # if we can not find a number samller than missing, so we have to patch it
                ## we can rearch every number missing+num[idx]
                missing += nums[idx]
                idx += 1
            else:
                # we add missing number, which we can get maximum is [s,2s - 1]
                missing *= 2
                patch += 1
        return patch