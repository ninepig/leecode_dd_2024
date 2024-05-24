class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_table = []
        for str in strs:
            cur = sorted(str)
            if cur in h_table:
                h_table[cur].append(str)
            else:
                h_table[cur] = []
                h_table[cur].append(str)

        res = []
        for key in h_table:
            res.append(h_table[key])

        return res


    def groupAnagramsAnswer(self, strs: List[str]) -> List[List[str]]:
        str_dict = dict()
        res = []
        for s in strs:
            sort_s = str(sorted(s))
            if sort_s in str_dict:
                str_dict[sort_s] += [s]
            else:
                str_dict[sort_s] = [s]

        for sort_s in str_dict:
            res += [str_dict[sort_s]]
        return res