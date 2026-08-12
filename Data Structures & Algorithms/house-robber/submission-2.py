class Solution:
    def rob(self, nums: List[int], cache = None) -> int:
        
        #you have two choice here either rob or skip for each house so to make the change you look at the proior house, but the change that we now need to store the result of robbing or not robbing. Failed dwon up bc of n-1 not n beingthe answer
        
        
        n  = len(nums)
        if n == 1: return nums[0]
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]

        



        

