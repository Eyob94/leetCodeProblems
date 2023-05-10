class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        while s:
            if s[0] not in t:
                return False
            else:
                ind = t.index(s[0])
                t = t[ind+1:] 
                s = s[1:]
                print(s, t)

        return True