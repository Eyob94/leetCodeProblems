class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            if r - l - max(count.values()) + 1 > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        
        return res


