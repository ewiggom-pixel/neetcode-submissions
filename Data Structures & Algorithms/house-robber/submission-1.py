class Solution:
    def rob(self, nums: List[int], cache = None) -> int:
        
        #you have two choice here either rob or skip for each house so to make the change you look at the proior house, but the change that we now need to store the result of robbing or not robbing
        
        
        n  = len(nums)
        memo = [-1] * n

        def recursive(i):

            if i < 0:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(recursive(i-1), recursive(i-2) + nums[i])
            return memo[i]
        return recursive(n-1)
        

