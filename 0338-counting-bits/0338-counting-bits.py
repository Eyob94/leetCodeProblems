class Solution:
    def countBits(self, n: int) -> List[int]:
        return list(bin(x)[2:].count('1') for x in range(n+1))