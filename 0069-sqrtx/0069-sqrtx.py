class Solution:
    def mySqrt(self, x: int) -> int:
        prev =0

        for i in range(x+1):
            if i*i <= x:
                prev = i
            else:
                break

        return (prev)