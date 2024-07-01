#https://www.fastprep.io/problems/amazon-get-k-rep-value


'''

The team of machine learning scientists at Amazon wants to improve Amazon's product recommendation system. Based on a user's purchase history, the objective is to generate some extensive features that will be given as input to the machine learning model. One of the new proposed features is a k-repetitiveness feature whose computation is described below.

The purchase history of a user with the products available on Amazon is available in the form of a string user_history where the ith character represents the category of the ith product purchased by the user. The length of string user_history is n. There is also a given integer k.

The value of the k-repetitiveness feature for the string user_history is defined as the maximum number of substrings of the given string such that some product category in that substring appeared at least k times.

Find the value of the k-repetitiveness feature for the given string user_history.

'''

'''
sliding windows
'''
class Solution:
    def getkRepValue(self, user_history, k):
        ans = 0
        n = len(user_history)
        distinct = set(list(user_history))
        for char in list(distinct):
            substrings = 0
            count = 0
            left = 0
            for right in range(n):
                if user_history[right] == char:
                    count += 1
                while count >= k:
                    substrings += n - right
                    if user_history[left] == char:
                        count -= 1
                    left += 1
            ans = max(ans, substrings)

        return ans

sol =Solution()
test  = "acaab"
k = 3
print(sol.getkRepValue(test,k))