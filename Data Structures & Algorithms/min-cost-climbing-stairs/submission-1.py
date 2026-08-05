class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #this is just top down dp i think
        n = len(cost)
        memo = {}
        

        def recursive(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(recursive(i+1),recursive(i+2))
            return memo[i]


        return min(recursive(0), recursive(1))

