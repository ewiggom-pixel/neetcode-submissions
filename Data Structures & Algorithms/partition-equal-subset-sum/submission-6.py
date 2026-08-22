class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums)
        if target % 2 != 0:
            return False

        target = target // 2
        memo = {}
        def dfs(i,target):
            if (i, target) in memo:
                return memo[(i, target)]
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False
            
            memo[(i, target)] = dfs(i + 1, target) or dfs(i+1, target - nums[i])
            return memo[(i, target)]

        return dfs(0,target)
            
            