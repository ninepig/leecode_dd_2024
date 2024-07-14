class Solution:
    ## pick happen before deliver
    ## we must deliver all order at the end
    ## can not deliver oder without pick
    ## Need ask if picking should in order or not
    ## P1 D1
    def is_valid(self,orders:list[str]):
        if not orders and len(orders) == 0:
            return False
        p_set = set()
        d_set = set()
        for order in orders:
            order_type = order[0]
            order_number = int(order[1])
            if order_type == 'P':
                if order_number in d_set:
                    return False ## D order shows earlier than P
                elif order_number in p_set:
                    return False ## duplicated pickup
                ## this condition for asending order only
                elif len(p_set) != 0 and order_number < max(p_set):
                    return False
                else:
                    p_set.add(order_number)
            elif order_type == 'D':
                if order_number in d_set:
                    return False ## duplicated deiliver
                elif order_number not in p_set:
                    return False ## d ealier than p
                else:
                    d_set.add(order_number)

        return p_set == d_set


    def allCombinationWithAsding(self,n:int):
        if n <= 0 :
            return []
        if n == 1 :
            return ['P1','D1']

        res = []
        picked = set()
        delivered = set()
        def dfs(res,cur_path,picked,delivered,n):
            if len(cur_path) == n*2 :
                res.append(cur_path) ## dfs ending when we have 2*n long path
                return

            for i in range(n):
                if i not in picked:
                    if len(picked)== 0 or i > max(picked): ## 这一行代表是否要按照顺序
                        picked.add(i)
                        dfs(res,cur_path + ['P' + str(i+1)],picked,delivered,n)
                        picked.remove(i)##back tracking

            # we use cur_path , so we can do two forloop to handle path
            for i in range(n):
                if i in picked and i not in delivered:
                        delivered.add(i)
                        dfs(res,cur_path + ['D' + str(i+1)],picked,delivered,n)
                        delivered.remove(i)
            return
        dfs(res,[],picked,delivered,n)

        return res

    ## infer process 1359
    ## we have 2 n element
    # the first item must be n
    # the rest pair could be 2n - 1
    # so total number (n*2- 1) * n
    def countOrders(self, n):
        res, mod = 1, 10 ** 9 + 7
        for i in range(2, n + 1):
            res = res * (i * 2 - 1) * (i * 2) / 2 % mod
        return res

if __name__ == '__main__':
    sol = Solution()
    # test1 = ["P1","P2","D1","D2"]
    # test2 = ["P1" "D1"]
    # test3 = ["P1", "D2", "D1", "P2"]
    # test4 = ["P2", "D1", "P1", "D1"]
    # test5 = ["P2", "P1", "D1", "D2"]
    # print(sol.is_valid(test5))
    # print(sol.is_valid(test2))
    # print(sol.is_valid(test3))
    # print(sol.is_valid(test5))
    print(sol.allCombinationWithAsding(3))