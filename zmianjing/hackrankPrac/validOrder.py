'''
Examples below:
[P1, P2, D1, D2]==>valid
[P1, D1, P2, D2]==>valid
[P1, D2, D1, P2]==>invalid
[P1, D2]==>invalid
'''


class solution:
    def isValid(self, order):
        ## santity check
        if not order or len(order) == 0 or len(order) % 2 != 0:
            raise Exception("wrong input")
        pick = set()
        deliver = set()

        for item in order:
            item_type = item[0]
            item_id = item[1:]
            if item_type == 'P':
                if item_id in pick or item_id in deliver:
                    print("Wrong, p order exists")
                    return False
                pick.add(item_id)
            elif item_type == 'D':
                if item_id not in pick or item_id in deliver:
                    print("wrong d id order")
                    return False
                deliver.add(item_id)

        return pick == deliver

    def printOutAllCombination(self, n: int):
        if n <= 0:
            raise Exception("wrong input")

        if n == 1:
            return ["P1", "D1"]

        res = []
        pick_set = set()
        deliver_set = set()

        def backTracking(n, res, pick, delived, current_path):
            if len(current_path) == 2 * n:
                res.append(current_path)
                return

            for i in range(1, n + 1):
                if i not in pick:
                    pick.add(i)
                    backTracking(n, res, pick, delived, current_path + ["P" + str(i)])
                    pick.remove(i)

            ## bug !!!! 1 not i
            # for i in range(i,n+1):
            for i in range(1, n + 1):
                if i in pick and i not in delived:
                    delived.add(i)
                    backTracking(n, res, pick, delived, current_path + ["D" + str(i)])
                    delived.remove(i)

            return

        backTracking(n, res, pick_set, deliver_set, [])

        return res

        # 3 refering how many different option

    # we have 2n number for res
    # so for first number we have 2n option , but p should be first , so we have n option
    # for rest , we have 2n-1 option
    # so res = 2n*(2n-1)/2  ==> n*(2n-1)
    # so for totall --> for i in range(n)
    # we times all value toghter
    def countOrders(self, n):
        res = 1
        for i in range(2, n + 1):
            res = res * (i * 2 - 1) * (i * 2) / 2
        return res


sol = solution()
test3 = ["P1", "D1"]
print(sol.printOutAllCombination(2))
