class Solution:
    def rob(self, nums: List[int], cahce = None) -> int:
        
        if len(nums) == 1:
            return nums[0]
         
        def rob_linear(houses):
            m = len(houses)
            memo = [-1] * m
            def recursive(i):

                if i < 0:
                    return 0
                if memo[i] != -1:
                    return memo[i]
                memo[i] = max(recursive(i-1), (recursive(i-2) + houses[i]))
                return memo[i]
            return recursive(m-1)
            
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))