class solution:
    def consequnceOne(self,num:list[int]):
        ## 要做连续的题，所以不能更改数组
        ## 一般都是一个local 变量 一个global变量来做
        if not num or len(num) == 0:return 0
        local_max = 0
        global_max = 0
        for item in num:
            if item == 0:
                global_max = max(local_max,global_max)
                local_max = 0
            else:
                local_max += 1

        return max(global_max,local_max)
