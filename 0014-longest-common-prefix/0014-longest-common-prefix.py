class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixes = {}

        smallestWord = min(strs, key=len)

        index = len(smallestWord)
        for i in strs:
            inn = 0
            if(i==smallestWord):
                continue
            for j, lett in enumerate(smallestWord):
                if(i[j]==lett):
                    inn += 1
                else:
                    if(inn<index):
                        index=inn
                    break

        return smallestWord[:index]

            
            

        