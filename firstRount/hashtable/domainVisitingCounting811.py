class Solution:
    #不知道为啥报错..
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_counter = dict()
        for cpdomian in cpdomains:
            domian_item = cpdomian.split(' ')
            count = int(domian_item[0])
            cur_domain_list =domian_item[1].split('.')

            for i in range(len(cur_domain_list) - 1 ,-1 ,- 1) :# visit from back to form domain 1 by 1
                temp_domain = cur_domain_list[i:]
                if temp_domain in visit_counter:
                    visit_counter[temp_domain] += count
                else:
                    visit_counter[temp_domain] = count
                    
       res = []
       for k,v in visit_counter:
           res.append(str(v) + ' ' + k )
       return res


    def subdomainVisits2(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains:
            return []

        times_dict = dict()
        for cpdomain in cpdomains:
            tiems, domain = cpdomain.split()
            tiems = int(tiems)

            domain_list = domain.split('.')
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