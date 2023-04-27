class Solution:
    def fib(self, n: int) -> int:
        return self.helper(n)

    def helper(self, n: int, memo={}):
        if n in memo:
            return memo[n]
        if n<=0:
            return 0
        elif n<=2:
            return 1
        memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]

        