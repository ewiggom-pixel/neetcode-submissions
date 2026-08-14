class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #we need to look at just adding the index to the target no? sike it the max so that is wrong
        
        goal = len(nums) - 1


        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0