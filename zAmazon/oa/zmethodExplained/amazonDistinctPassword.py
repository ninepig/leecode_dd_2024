# https://www.fastprep.io/problems/amazon-find-encrypted-password
# two question， upper one should for ng only
# https://www.fastprep.io/problems/amazon-count-distinct-passwords
## 这个题python的做法 没有理由。
##改写成这个 https://github.com/Ivy678/Leetcode/blob/741d0c60f24d63fc2ba43936f4074be36b6f2b4f/amazon%20oa/countDistinctPassword.java#L4
'''
Weak passwords are likely to be hacked and misused. Due to this, developers at Amazon regularly come up with new algorithms to check the health of user passwords. A new algorithm estimates the variability of a password as the number of distinct password strings that can be obtained by reversing any one substring of the original password. Given the original password that consists of lowercase English characters, find its variability.

Note: A substring is a contiguous sequence of characters within a string. For example 'bcd', 'a', 'abcd' are substrings of the string 'abcd' whereas the strings 'bd', 'acd' are not.

'''

from collections import Counter
class Solution:
  def countDistinctPasswords(self, password: str) -> int:
    n, c = len(password), Counter(password)
    total = 1
    for v in c.values():
        total+=v*(n-v)
        n-=v
    return total


  def countBurtalWay(self,password:str)-> int:
      dis_password = set()
      dis_password.add(password)
      for i in range(len(password)):
          for j in range(i + 1 ,len(password)):
              replace_string = password[i:j+1]
              replace_string_Rev = replace_string[::-1]
              new_pass = password[:i] + replace_string_Rev + password[j+1:]
              dis_password.add(new_pass)

      return len(dis_password)




password = "abc"
# password = "abab";
# password = "abaa"
sol = Solution()
print(sol.countDistinctPasswords(password))
print(sol.countBurtalWay(password))












'''
class Solution {
    public long countDistinctPasswords(String password) {
        // A set to keep all the distinct passwords
        Set<String> distinctPasswords = new HashSet<>();
        
        // Add the original password to the set
        distinctPasswords.add(password);
        
        // Iterate through all possible substrings
        for (int i = 0; i < password.length(); i++) {
            for (int j = i + 1; j <= password.length(); j++) {
                StringBuilder newPassword = new StringBuilder(password);
                // Reverse the substring and form a new password
                String reversedSubstring = new StringBuilder(password.substring(i, j)).reverse().toString();
                newPassword.replace(i, j, reversedSubstring);
                
                // Add the newly formed password to the set
                distinctPasswords.add(newPassword.toString());
            }
        }
        
        return distinctPasswords.size();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        String password = "abc";
        System.out.println(s.countDistinctPasswords(password));

        password = "abaa";
        System.out.println(s.countDistinctPasswords(password));

        password = "abab";
        System.out.println(s.countDistinctPasswords(password));
    }
    
    
}
'''