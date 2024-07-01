'''
You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.
Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.
Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).

'''
import collections
from typing import List

## TODO time analysis
'''
这个题比较复杂。 
1 要找到根据时间排序 ， user的浏览记录
2 根据这些浏览记录， 统计长度大于2 连续的 （w1,w2,w3) tuble
3 统计tuble的数量，最大的是答案。 如果even 那就是按照网站的字典排序
'''

class solution:
    def mostVisitedPatternWenjing(self,timestamp:list[str],username:list[str],website:list[str]):
        user_website_dict = collections.defaultdict(list) ## each user - website list dict
        website_record = sorted(zip(timestamp,username,website),key= lambda x:x[0]) ## sorted a website record, by timestamp

        for item in website_record:
            _,user,site = item[0],item[1],item[2]
            user_website_dict[user].append(site)

        print(user_website_dict)
        ## we count (w1,w2,w3)'s show up times
        website_tuble_count = collections.defaultdict(int)

        for website_list in user_website_dict.values():
            s = set() ## help set to remove duplcated
            cur_size = len(website_list)
            if cur_size > 2:
                for i in range(cur_size - 2):
                    for j in range(i + 1 , cur_size - 1):
                        for k in range(j + 1 , cur_size):
                            s.add((website_list[i],website_list[j],website_list[k]))

            for t in s :
                ## for each tumble , put in to dict counter
                website_tuble_count[t] += 1

        ## count the most item if there is even count , sort by alphabeta

        items = website_tuble_count.items()
        print(items)
        ## we sorted {():x} dict by value desending first , then asdeng
        return sorted(items,key=lambda x:(-x[1],x[0]))[0][0]
        # return items


if __name__ == "__main__":
    user = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
    timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    website = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
    # Output: ["home", "about", "career"]
    sol = solution()
    print(sol.mostVisitedPatternWenjing(timestamp,user,website))
