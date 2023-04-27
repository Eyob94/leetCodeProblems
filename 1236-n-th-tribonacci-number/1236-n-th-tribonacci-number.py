class Solution:
    def tribonacci(self, n: int) -> int:
        return self.helper(n)

    def helper(self, n, memo={}):
        if n in memo:
            return memo[n]
        elif n <= 0:
            return 0
        elif n <= 2:
            return 1
        memo[n] = self.helper(n-1, memo)+ self.helper(n-2, memo)+ self.helper(n-3, memo)
        return memo[n]