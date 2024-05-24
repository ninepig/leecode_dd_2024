class monoTemplate:
    ## 单调栈复杂的题目一般用index作为元素入栈。 这样可以作为pointer去原数组进行查询
    ## 可以从左往右，也可以从右往左 ， 非常非常灵活
    def monoStack(self,nums:list[int]):
        stack = []
        for i,v in enumerate(nums):
            ## 单调递增栈， 如果比当前栈顶元素大， 出栈 再入栈 这样栈顶元素出栈
            while stack and stack[-1] <= v : ## increasing(top to bottom) monostack
                stack.pop(...) ## 栈顶元素pop的时候 ，第一个比它大的元素就是v
            if stack :
                ## v 也就是当前元素。 他入栈之时，如果栈不为空，则他左侧第一个比它大的元素就是栈顶
                v_bigger = stack[-1] ##
            stack.append(...)
    def monoStackDecreasing(self,nums:list[int]):
        stack = []
        for i, v in enumerate(nums):

            while stack and stack[-1] >= v : ## decreasing(top to bottom)
                stack.pop() ## 栈顶pop的时候， 右侧第一个比他小的元素就是当前元素v

            if stack :
                v_smaller = stack[-1] ##  v 也就是当前元素。 他入栈之时，如果栈不为空，则他左侧第一个比它小的元素就是栈顶

            stack.append(...)




'''
所以单调栈一般用于解决一下几种问题：

寻找左侧第一个比当前元素大的元素。
寻找左侧第一个比当前元素小的元素。
寻找右侧第一个比当前元素大的元素。
寻找右侧第一个比当前元素小的元素。
下面分别说一下这几种问题的求解方法。

2.1 寻找左侧第一个比当前元素大的元素
从左到右遍历元素，构造单调递增栈（从栈顶到栈底递增）：
一个元素左侧第一个比它大的元素就是将其「插入单调递增栈」时的栈顶元素。
如果插入时的栈为空，则说明左侧不存在比当前元素大的元素。
2.2 寻找左侧第一个比当前元素小的元素
从左到右遍历元素，构造单调递减栈（从栈顶到栈底递减）：
一个元素左侧第一个比它小的元素就是将其「插入单调递减栈」时的栈顶元素。
如果插入时的栈为空，则说明左侧不存在比当前元素小的元素。
2.3 寻找右侧第一个比当前元素大的元素
从左到右遍历元素，构造单调递增栈（从栈顶到栈底递增）：

一个元素右侧第一个比它大的元素就是将其「弹出单调递增栈」时即将插入的元素。
如果该元素没有被弹出栈，则说明右侧不存在比当前元素大的元素。
从右到左遍历元素，构造单调递增栈（从栈顶到栈底递增）：

一个元素右侧第一个比它大的元素就是将其「插入单调递增栈」时的栈顶元素。
如果插入时的栈为空，则说明右侧不存在比当前元素大的元素。
2.4 寻找右侧第一个比当前元素小的元素
从左到右遍历元素，构造单调递减栈（从栈顶到栈底递减）：

一个元素右侧第一个比它小的元素就是将其「弹出单调递减栈」时即将插入的元素。
如果该元素没有被弹出栈，则说明右侧不存在比当前元素小的元素。
从右到左遍历元素，构造单调递减栈（从栈顶到栈底递减）：

一个元素右侧第一个比它小的元素就是将其「插入单调递减栈」时的栈顶元素。
如果插入时的栈为空，则说明右侧不存在比当前元素小的元素。
上边的分类解法有点绕口，可以简单记为以下条规则：

无论哪种题型，都建议从左到右遍历元素。

查找 「比当前元素大的元素」 就用 单调递增栈，查找 「比当前元素小的元素」 就用 单调递减栈。

从 「左侧」 查找就看 「插入栈」 时的栈顶元素，从 「右侧」 查找就看 「弹出栈」 时即将插入的元素。

'''

