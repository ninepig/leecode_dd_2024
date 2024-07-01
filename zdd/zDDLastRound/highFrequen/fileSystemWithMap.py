class SolutionMap:
    def __init__(self):
        self.file_value_map = {"":-1}
    def createPath(self,paths:str, val:str):
        if paths in self.file_value_map:
            ## it exists
            return False
        ## if prefix not exist
        if not paths[:paths.rindex("/")] in self.file_value_map:
            return False
        self.file_value_map[paths] = val #
        return True

    def getPathValue(self,paths):
        if paths in self.file_value_map:
            return self.file_value_map[paths]
        else:
            return -1

    ## need ask what happen if there is children exist?
    ## if this is required, we need check before delete
    ## if any key contain this path in map. if contain. delete
    ## delete 就麻烦一点。如果删除的是父亲path
    # 比如、/LEET/CODE 删除leet 那leetcode也要删掉
    def deletePath(self,paths):
        contain = False
        delete_key = []
        ## TODO 这个逻辑有问题。。需要问清楚， 除非是start with。要不然不该删除， 而不是in
        for key in self.path_file_dict.keys():
            # if paths in key: ## 这个有问题
            ## 应该是这样的
            if key.startswith(paths):
                # To avoid runtime error
                ##     for key in self.path_file_dict.keys():
                # RuntimeError: dictionary changed size during iteration
                # del self.path_file_dict[key]
                delete_key.append(key)
                contain = True
        for delete_path in delete_key:
            del self.path_file_dict[delete_path]
        if not contain:
            return "not contain"
        else:
            return "successed"

