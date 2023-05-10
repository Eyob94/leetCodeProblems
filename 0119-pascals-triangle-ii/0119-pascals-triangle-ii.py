class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1], [1, 1]]
        if rowIndex <=1:
            return dp[rowIndex]

        for i in range(2, rowIndex+1):
            l = [0]*(i+1)
            l[0], l[-1] = 1, 1
            for j in range(1, len(l)-1):
                l[j] = dp[i-1][j-1] + dp[i-1][j]
            dp.append(l)

        return dp[rowIndex]
