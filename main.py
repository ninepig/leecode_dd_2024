# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections
import heapq

from LinkedList import List


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(ord('A'))
    # pq = []
    # heapq.heappush(pq,(5,8))
    # heapq.heappush(pq, (3, 2))
    # heapq.heappush(pq, (1, 1))
    # heapq.heappush(pq, (7, 4))
    #
    # print(len(pq))
    # for _ in range(len(pq)):
    #     val, i = heapq.heappop(pq)
    #     print(val, i)
    # sampleDict = collections.defaultdict(int)
    # sampleDict = {}
    # test = "abc"
    # for char in test:
    #     if char not in sampleDict:
    #         sampleDict[char] = 1
    #     else:
    #          sampleDict[char] += 1
    # print(sampleDict)
    # string = "/a/b/c"
    # str= string.split("/")
    # print(str[1:-1])

    # nums = [1, 2, 3, 4]
    # size = len(nums)
    # res = [1 for _ in range(size)]
    #
    # left = 1
    # for i in range(size):
    #     res[i] *= left
    #     left *= nums[i]
    #
    # print(res)
    # nums = [2, 3, 4, 5]
    # sorted(nums, key=lambda num: abs(4 - num))
    # nums.sort(key=lambda v: abs(v - 4))

    # nums = nums + nums

    # points = [[2,3],[1,2],[2,-2],[1,-3]]
    # points.sort(key=lambda x:(x[0], x[1]))
    list = []
    list_test = [1,2,3,4]
    list_test2 =[2,3,4,5]
    print(list_test[:])
    list.append(list_test[:])
    list.append(list_test2)
    print(list)
    s = "aabdd"
    memo = collections.defaultdict(int)
    # python的写法问题
    for char in s:
        memo[char] += 1
    print(memo)
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

    #自己写的 ,这个逻辑不对 ， python 的del dict key 必须是 del dict[key]
    def delete(self,s)->bool:
        node = self
        parent = None
        lastPath = None
        paths = s.split('/')
        for path in paths:
            if path not in node.children:
                return False
            node= node.children[path]
            parent = node
            lastPath = path
        del parent[lastPath] ## delete LastNode, this node has value
        return True
