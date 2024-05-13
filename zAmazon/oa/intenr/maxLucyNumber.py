#https://www.fastprep.io/problems/max-lucky-numbers
'''
Amazon.com is distributing coupons in the form of a lottery system for loyal customers. The coupons are called "lucky numbers" and the customer with the largest lucky number gets the best discount. Devise a method to determine the maximum possible lucky number. A positive integer is a lucky number if its decimal representation contains only digits x and y. For example, if x=2 and y=5, then 2, 552, and 5225 are lucky numbers, and 3, 24, 57 and 389 are not.

For example, if x=2 and y=5, then 2, 552, and 5225 are lucky numbers, and 3, 24, 57 and 389 are not.

Given two different digits x and y and a positive integer n, determine the maximum possible lucky number, the sum of whose digits is n. It is guaranteed that at least one lucky number exists for the given x, y, and n.
'''


'''
int max = 0;
public int getMaxLuckyNumber(int x, int y, int n) {
    dfs(x, y, 0, 0, n);
    return max;
}

private void dfs(int x, int y, int num, int sum, int n) {
  if (sum > n) return;
  if (sum == n) {
    max = Math.max(max, num);
  }

  dfs(x, y, num * 10 + x, sum + x, n);
  dfs(x, y, num * 10 + y, sum + y, n);
}
'''