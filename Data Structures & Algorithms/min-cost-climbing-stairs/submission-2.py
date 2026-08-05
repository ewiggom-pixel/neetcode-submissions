class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #this is just top down dp i think
        n = len(cost)
        memo = {}
        

        #def recursive(i):
            #if i >= len(cost):
                #return 0
            #if i in memo:
                #return memo[i]
            
            #memo[i] = cost[i] + min(recursive(i+1),recursive(i+2))
            #return memo[i]


        #return min(recursive(0), recursive(1))
        
        array = [0] * (n+1)
        
        def recursive_down(i):

            for i in range(2,n+1):
                array[i] = min(array[i-1] + cost[i-1], array[i-2] + cost[i-2])
            return array[n]

        return recursive_down(n)