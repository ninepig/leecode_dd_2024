'''

Pick & Delivery Permutations
1. https://leetcode.com/discuss/interview-question/1149234/DoorDash-Phone-Interview
2. https://leetcode.com/discuss/interview-question/1245761/DoorDash-Onsite
3. https://leetcode.com/discuss/interview-question/1142755/DoorDash-or-E4-or-Phone-Screen-or-Virtual-Onsite-Offer
4. https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

A driver's route can be represented as follows:
Given a set list of pickups and deliveries for order, figure out if the given list is valid or not.

A delivery cannot happen for an order before pickup.
The same order cannot be delivered or picked up twice
The car must be empty at the end of the drive.

##Pick are ascending order and delivery can be any order ？？

Examples below:
[P1, P2, D1, D2]==>valid
[P1, D1, P2, D2]==>valid
[P1, D2, D1, P2]==>invalid
[P1, D2]==>invalid
[P1, P2]==>invalid
[P1, D1, D1]==>invalid
[]==>valid
[P1, P1, D1]==>invalid
[P1, P1, D1, D1]==>invalid
[P1, D1, P1]==>invalid
[P1, D1, P1, D1]==>invalid

## 我觉得这个题 p1 必须 p2之前这个case 不解决 那就很难 所以要validate
## Pick are ascending order and delivery can be any order ## 如果有这个条件 那就先检查下这个就行了。 如果不valid 就是false
1 check if valied
2 print all permutation 第二小题 如果要做到 p1 必须 在p2 之前就挺难的
3 find longest valid path (如果是这个的话。。hashmap不就能解决吗)
4 推导所有数量的过程 https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/ rareleetcode 原题

目前看到这题有两种变形
第一种感觉比较少
1 pickup 需要排序 也就是 p1 在p2 前面 2 follwup all permutation

第二种
1 任意pick up order 不需要排序
  followup 1 permutation 2 推导 公式 3 一亩三分地上有说是621的 但是我感觉不是。 应该是1359的推导 因为这个明显没有duration 这个概念。 但是可以把那个写一下
'''

##todo missing thinking 2longest sub array with o(n) time ?

## https://leetcode.com/discuss/interview-question/1146195/DoorDash-or-Software-Engineer-or-Full-Interview

# 似乎还需要重新看下
class Solution:
    ## pick happen before deliver
    ## we must deliver all order at the end
    ## can not deliver oder without pick
    def is_valid(self,order:list[str]):
        if not order or len(order) == 0:
            return False
        if len(order) == 1 :
            return False
        if len(order) == 2 :
            return order == ["P1","D1"]

        ## 如果需要考虑 p2 必须在p1之后出现 加一个
        if not self.is_validwithPasding(order):
            return False

        pick_set = set()
        delivery_set = set()

        for item in order:
            item_type,number = item[0],item[1:]
            if item_type == 'P':
                if number in pick_set:
                    # duplicated pick
                    return False
                elif number in delivery_set:
                    ## deliver before pick , not right
                    return False
                else:
                    pick_set.add(number)

            if item_type == 'D':
                if number in delivery_set:
                    ## duplicated order
                    return False
                elif number not in pick_set:
                    ## deliver before pick
                    return False
                else:
                    delivery_set.add(number)

        return pick_set == delivery_set

    ##  if we need pick up as order asdending
    def is_validwithPasding(self, order: list[str]):
        p_number_list = []

        for item in order:
            if item[0] == 'P':
                p_number_list.append(int(item[1:]))
        sorted_list = sorted(p_number_list)

        return sorted_list ==p_number_list

    ## all pick and deliver without order combinadtion
    def allCombination(self,n:int):
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
                    if len(picked)== 0 or i > max(picked):
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
    ## 最长的 valid 数组 但是感觉只有leetcode上出现过一次 可能是傻逼理解错了？
    ## TODO, o(n2)的暴力法 可以解 if we dont care valid time
    ## 不确定有没有这道题
    ## TODO sliding windows？ o(n)  treat this as a sliding windows

if __name__ == '__main__':
    sol = Solution()
    # test1 = ["P1","P2","D1","D2"]
    # test2 = ["P1" "D1"]
    # test3 = ["P1", "D2", "D1", "P2"]
    # test4 = ["P1", "D1", "P1", "D1"]
    # test5 = ["P1", "P2", "D1", "D2"]
    # print(sol.is_valid(test1))
    # print(sol.is_valid(test2))
    # print(sol.is_valid(test3))
    # print(sol.is_valid(test5))
    print(sol.allCombinationWithAsding(4))
    # print(sol.is_validwithPasding(["P1","P12","P2"]))


