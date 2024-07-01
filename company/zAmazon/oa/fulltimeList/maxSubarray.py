'''
1. Code Question:

Amazon Web Services (AWS) offers learning opportunities for computer science students in a series of courses.
Upon completing a course, AWS awards the student with an electronic learning badge.
Before signing up for further courses, a student assigns each badge a value based on interest:

    * 1 means that the student is interested
    * -1 means that the student is not interested

To perform some analysis on the students' interest in the courses, given the array badges and their elements,
either 1 or -1, find a subarray of maximum length such that the product (multiplications) of all the elements in the subarray is 1.

A subarray is a contiguous group of elements in an array.

Example
There are 6 subjects:
1: Security
2: Networking
3: Machine Learning
4: IoT
5: DBMS
6: Analytics

badges = [1, -1, -1, 1, 1, -1]

The student is interested in Security, IoT, and DBMS as indicated in the badges array.

These are a few of the subarrays whose multiplication is equal to 1. Note that * represents the multiplication sign in the example below

    • beginning and ending indices (0, 0) i.e. 1, the length of the subarray is 1
    • indices (0, 4) i.e. 1 * -1 * -1 * 1 * 1 = 1, the length of the subarray is 5
    • indices (1, 4) i.e. -1 * -1 * 1 * 1 = 1, the length of the subarray is 4
    • indices (1, 2) i.e. -1 *-1 = 1, the length of the subarray is 2

The maximum subarray length whose product is equal to 1 is length 5. Return 5.

Function Description
Complete the function maxSubarrayLength in the editor below.

maxSubarrayLength has the following parameter:
int badges[n]: the student's interest in each of the subjects, either 1 or -1

Returns
int: the maximum length subarray with a product of 1

There will be at least one non-empty subarray that satisfies the given condition.

Sample Case 0
badges size, n = 6
badges = [1, -1, -1, -1, 1, 1]
output = 4

Explanation
These are a few of the subarrays whose product is equal to 1:
    • Subarray with indices from (0, 2), length of the subarray is 3.
    • Subarray with indices from (1, 2), length of the subarray is 2.
    • Subarray with indices from (2, 5), length of the subarray is 4.
    • Subarray with indices from (4, 5), length of the subarray is 2.
The maximum subarray length whose product is equal to 1 is length 4.

Sample Case 1
badges size, n = 4
badges = [-1, 1, -1, 1]
output = 4

Explanation
Here, the optimal solution is to choose the entire array as the subarray because its
product is 1.



'''
def maxSubarrayLength(badges):
    answer, positive, negative = 0, 0, 0

    for interested in badges:
        if interested == 1:
            positive += 1
            if negative > 0:
                negative += 1
        else:  # interested == -1
            negative, positive = positive + 1, (
                negative + 1 if negative > 0 else 0)

        answer = max(positive, answer)
    return answer


if __name__ == '__main__':
    print(maxSubarrayLength([-1, 1, -1, 1]))