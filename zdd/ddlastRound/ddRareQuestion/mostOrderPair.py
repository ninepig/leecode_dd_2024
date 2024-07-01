'''
1.非leetcode他自己出的题，给你很多订单
订单1， 可乐，可乐，汉堡，薯条
订单2，汉堡，牛奶，苹果，可乐
类似上面那种，要你找出点的最频繁的pair，比如以上这种情况最火爆的就是（可乐汉堡）这个组合
'''
import collections

## todo 是否会出现duplicate？
class solution:
    def getMostOrderItemPair(self,orders:list[list[str]]):
        order_dict = collections.defaultdict(int)
        for order in orders:
            order_length = len(order)
            for i in range(order_length):
                for j in range(i + 1 , order_length):
                    order_pair = (order[i],order[j])
                    order_dict[order_pair] += 1
        res = []
        print(order_dict)
        max_value = max(order_dict.values())
        for key,value in order_dict.items():
            if value == max_value:
                res.append(key)

        return res

if __name__ == "__main__":
    order1 = ["a","b","c","d"]
    order2 = ["a","b","f","g"]
    order3 = ["a","b","g","h"]
    order_list= []
    order_list.append(order1)
    order_list.append(order2)
    order_list.append(order3)
    sol = solution()
    print(sol.getMostOrderItemPair(order_list))