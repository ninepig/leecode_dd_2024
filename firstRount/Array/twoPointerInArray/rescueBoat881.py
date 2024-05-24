'''
贪心+双指针

暴力枚举的时间复杂度为
。使用双指针可以减少循环内的时间复杂度。

我们可以利用贪心算法的思想，让最重的和最轻的人一起走。这样一只船就可以尽可能的带上两个人。

具体做法如下：

先对数组进行升序排序，使用 ans 记录所需最小船数。
使用两个指针 left、right。left 指向数组开始位置，right 指向数组结束位置。
判断 people[left] 和 people[right] 加一起是否超重。
如果 people[left] + people[right] > limit，则让重的人上船，船数量 + 1，令 right 左移，继续判断。
如果 people[left] + people[right] <= limit，则两个人都上船，船数量 + 1，并令 left 右移，right 左移，继续判断。
如果 lefft == right，则让最后一个人上船，船数量 + 1。并返回答案。
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        size = len(people)
        left, right = 0, size - 1
        ans = 0
        while left < right:
            if people[left] + people[right] > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            ans += 1
        if left == right:
            ans += 1
        return ans