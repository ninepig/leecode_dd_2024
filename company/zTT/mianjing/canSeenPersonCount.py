'''
There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.


https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/


Explanation
We maintain a decreasing mono stack,
(I stored the index of elements)

As we iterate each element a in input array A,
assume the last element in the stack has index i.
If the last element A[i] <= a,
A[i] can see a,
so we increment res[i]++

Because a is tall and block the line of sight.
A[i] can't see any element after a,
we have done the work for A[i],
so we stack.pop() it from the stack.

We keep doing this while A[i] < a, where i = stack.top().
By doing this, if stack is not empty,
A[i] will be the left next greater element of a.
A[i] can still see a,
so we increment res[i]++.

We do the above for each element a in A,
and we finally return result res



https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=1067611&page=1#pid19559606
Mary is walking down a street with n tall buildings lined up.
Calculate how many buildings she can see from each building.
For example,
input: [5,3,8,3,2,5]
seen from left[2, 1, 2, 2, 1, 0]
seen from right [0, 1, 2, 1, 1, 3]
Output: [3,3,5,4,4,4]
'''
from typing import List


'''
这道题是复杂的单调栈题目 不是单纯的找左侧或者右侧第一个大或者小的
而是应用题。。 面试的时候估计没做过 想不出来
'''
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []
        res2 = [0] * len(heights)

        ## canSee from left
        for i, v in enumerate(heights):
            ## monotoic decreasing stack
            ## if there is a value bigger than top in stack
            ## it can only see this bigger value. So we pop out index, can increasing that index seeing value by 1
            ## we found top item who is bigger than current item(if that eixst), we increase that by 1.

            while stack and heights[stack[-1]] <= v:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        print(res)
        ## canSeen from right
        stack2 = []
        for i ,v in enumerate(heights[::-1]):
            new_index = len(heights) - 1 - i
            while stack2 and heights[stack2[-1]] <= v:
                res2[stack2.pop()] += 1
            if stack2:
                res2[stack2[-1]] += 1
            stack2.append(new_index)
        print(res2)
        return res ## res +res2

sol = Solution()
inputs = [5,3,8,3,2,5]
sol.canSeePersonsCount(inputs)


# input: [5,3,8,3,2,5]
# seen from left[2, 1, 2, 2, 1, 0]
# seen from right [0, 1, 2, 1, 1, 3]

# for i, v in enumerate(inputs[::-1]):
#     print(len(inputs)-i - 1,v)
