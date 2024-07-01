class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = dict()
        for str in strs:
            sorted_str = sorted(str)
            if sorted_str in sorted_dict:
                sorted_dict[sorted_str] += [sorted_str] #python 小技巧
            else:
                sorted_dict[sorted_str] = [sorted_str]
        res =[]
        for key in sorted_dict.keys():
            res.append(sorted_dict[key])

        return res