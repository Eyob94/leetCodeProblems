class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        curr = 0
        prev = 0
        sum = 0

        for i in s[::-1]:
            curr = romans[i]
            if prev>curr:
                sum-=curr
            else:
                sum+=curr
            
            prev = curr
        
        return sum