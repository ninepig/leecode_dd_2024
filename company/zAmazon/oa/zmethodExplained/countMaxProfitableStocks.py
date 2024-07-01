#https://www.fastprep.io/problems/count-maximum-profitable-groups

'''
A team of analysts at Amazon needs to analyze the stock prices of Amazon over a period of several months.

A group of consecutively chosen months is said to be maximum profitable
if the price in its first or last month is the maximum for the group.
More formally, a group of consecutive months [l, r] (1 ≤ l ≤ r ≤ n) is said to be maximum profitable if either:

stockPrice[l] = max(stockPrice[l], stockPrice[l + 1], ..., stockPrice[r])
or, stockPrice[r] = max(stockPrice[l], stockPrice[l + 1], ..., stockPrice[r])
Given prices over n consecutive months, find the number of maximum profitable
groups which can be formed. Note that the months chosen must be consecutive, i.e., you must choose a subarray of the given array.
'''
from typing import List


def countSubArray(nums: List[int]) -> int:
    prevGreater = [-1] * len(nums)
    prevNonSmaller = [-1] * len(nums)
    prevNonSmallerCount = [1] * len(nums)

    stack = []
    for (i, num) in enumerate(nums):
        while stack and nums[stack[-1]] <= num:
            stack.pop()
        if stack:
            prevGreater[i] = stack[-1]
        stack.append(i)

    stack = []
    for (i, num) in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            stack.pop()
        if stack:
            prevNonSmaller[i] = stack[-1]
        stack.append(i)

    for i in range(len(nums)):
        if prevNonSmaller[i] >= 0:
            prevNonSmallerCount[i] = 1 + \
                prevNonSmallerCount[prevNonSmaller[i]]

    ans = 0
    for i in range(len(nums)):
        prev = prevGreater[i]
        ans += i - prev
        if prev >= 0:
            ans += prevNonSmallerCount[prev]
    return ans

'''
The algorithm initializes a count variable to 0, which tracks the total number of maximum profitable groups.
It iterates through each month, considering it as the start of a potential group. Every individual month is also considered a maximum profitable group by itself, so count is incremented immediately in each iteration.
For each starting month, it looks ahead to all possible end months to form groups. Two conditions are checked:
If an end month's stock price exceeds the current max, it updates max and increments count since this forms a new maximum profitable group.
Additionally, if the start month's stock price equals max (implying it hasn't been exceeded by any month in between), count is incremented again for each of these scenarios.
'''
def countMaxGroup(stockList:list[int])->int:
    count = 0

    for i in range(len(stockList)):
        start = stockList[i]
        max = start
        count += 1
        for j in range(i+1,len(stockList)):
            end = stockList[j]
            if end > max :
                max = end
                count += 1
            elif start == max:
                count += 1

    return count

# print(countSubArray([3, 1, 3, 5]), 10)
# print(countSubArray([1, 3, 2]), 5)
# print(countSubArray([8, 9, 5, 3, 7]), 12)
# print(countSubArray([10, 8, 9, 5, 3, 7]), 18)
# print(countSubArray([1, 2, 3, 4, 5, 6]), 21)
# print(countSubArray([1, 1, 2, 2, 3, 3]), 21)

print(countMaxGroup([3, 1, 3, 5]))
print(countMaxGroup([1, 5, 2]))
print(countMaxGroup([2, 3, 2]))

'''
public long countMaximumProfitableGroups(int[] stockPrice) {
    // List to potentially store all groups (unused in the final count)
    // List<List<Integer>> allGroups = new ArrayList<>();
    int count = 0; // Initialize the count of maximum profitable groups
    
    // Iterate through each month in the stockPrice array
    for (int i = 0; i < stockPrice.length; i++) {
        int start = stockPrice[i]; // Current starting month's stock price
        int max = start; // Initialize max as the starting month's stock price
        // List<Integer> group = new ArrayList<>(); // Group formation (unused)
        count++; // Count the current month as a profitable group by itself
        
        // Extend the group to include months following the start month
        for (int j = i + 1; j < stockPrice.length; j++) {
            int end = stockPrice[j]; // Current ending month's stock price
            
            // If the ending month's stock price is greater than max, it becomes the new max
            if (end > max) {
                max = end;
                count++; // Count this as a new maximum profitable group
            } 
            // If the starting month's stock price is still the max, count a new group
            else if (start == max) {
                count++;
            }
        }
    }
    
    return count; // Return the total count of maximum profitable groups
}
'''