class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in strs:
            ind = ''.join(sorted(i))
            if ind in dic.keys():
                dic[ind].append(i)
            else:
                dic[ind] = [i]

           
        
        return dic.values()