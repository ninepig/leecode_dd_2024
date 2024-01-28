#
#
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains:
            return []

        times_dict = dict()
        for cpdomain in cpdomains:
            tiems, domain = cpdomain.split()
            tiems = int(tiems)

            domain_list = domain.split('.')
            # 从后往前，stop = -1 代表到头部 在range 之中步长 1
            for i in range(len(domain_list) - 1, -1, -1):
                sub_domain = '.'.join(domain_list[i:])
                if sub_domain not in times_dict:
                    times_dict[sub_domain] = tiems
                else:
                    times_dict[sub_domain] += tiems

        res = []
        for key in times_dict.keys():
            res.append(str(times_dict[key]) + ' ' + key)
        return res


# domain= "discuss.leetcode.com"
# domain_list = domain.split('.')
# print(domain_list[-1])
# array = [1,2,3,3,4,5,6,7]
# for i in range(len(domain_list) - 1, -1, -1):
#     sub_domain = '.'.join(domain_list[i:])
#     print(sub_domain)
# array = [1,2,3,3,4,5,6,7]
# for i in range(len(array) - 1, -1, -1):
#     print(array[i])