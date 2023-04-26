class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r = 0, 1
        lgth = len(s)

        for i in range(lgth):
            for j in range(lgth, i, -1):
                tmp = s[i:j]
                if tmp == tmp[::-1] and j-i > r-l:
                    l, r = i, j
                    break
            if(len(s)-i < r-l):
                break
          
        return s[l:r]
            