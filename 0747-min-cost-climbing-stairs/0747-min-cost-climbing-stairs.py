class Solution:      

    def minCostClimbingStairs(self, cost: List[int], memo={}) -> int:
        if tuple(cost) in memo:
            return memo[tuple(cost)]
        if len(cost) <= 1:
            return 0
        
        cost1 = cost[0] + self.minCostClimbingStairs(cost[1:], memo)
        cost2 = cost[1] + self.minCostClimbingStairs(cost[2:], memo)

        memo[tuple(cost)] = min(cost1, cost2)

        return memo[tuple(cost)]


        
    