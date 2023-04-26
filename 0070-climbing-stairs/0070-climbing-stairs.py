class Solution:
    def climbStairs(self, n: int) -> int:
        sum = 0
        a, b = 0, 1

        for i in range(n):
                a,b = b, b+a

        return b

            