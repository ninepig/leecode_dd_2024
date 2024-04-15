import collections


class Solution:

    def getMostPairs(self, order_list):
        ## santity check
        if not order_list or len(order_list) == 0:
            raise Exception("invalid input")
        pair_order_dict = collections.defaultdict(int)
        for orders in order_list:
            for i in range(len(orders)):
                for j in range(i + 1, len(orders)):
                    pair = (orders[i], orders[j])
                    pair_order_dict[pair] += 1
        res = []
        most_number = max(pair_order_dict.values())
        for k, v in pair_order_dict.items():
            if v == most_number:
                res.append(k)

        return res

    def getMostOrderPair(self, orders: list[list[str]]):
        if not orders and len(orders) == 0:
            return []
        pair_order_dict = collections.defaultdict(int)
        for order in orders:
            order_combine = self.getKcombine(order, 2)
            for item in order_combine:
                ## we need convert list to a tumble , then make that as key in dict
                item_tuple = tuple(item)
                pair_order_dict[item_tuple] += 1

        max_number = 0

        res = []
        most_number = max(pair_order_dict.values())
        for k, v in pair_order_dict.items():
            if v == most_number:
                res.append(k)

        return res

    def getKcombine(self, target: list[str], k: int):
        res = []

        def backtrack(idx, current_path, res):
            if len(current_path) == k:
                res.append(current_path.copy())
                return
            for i in range(idx, len(target)):
                current_path.append(target[i])
                ## 这里要是i 不是idx！！ bug bug bug bug！！
                backtrack(i + 1, current_path, res)
                current_path.pop()

        backtrack(0, [], res)
        return res


test = ["milk", "apple", "burger", "dick"]
test2 = ["milk", "apple", "pick", "dog"]
test3 = ["milk", "apple", "bird", "pig"]
test_array = [test, test2, test3]

sol = Solution()
print(sol.getMostPairs(test_array))
print(sol.getMostOrderPair(test_array))