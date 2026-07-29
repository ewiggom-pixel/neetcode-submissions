class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        combs = []
        self.helper(0, [], combs, nums, target)
        return combs

    def helper(self, i, curComb, combs, nums, target):
        if sum(curComb) == target:
            combs.append(curComb.copy())
            return
        if i >= len(nums) or sum(curComb) > target:
            return
    
        curComb.append(nums[i])
        self.helper(i, curComb, combs, nums, target)
        curComb.pop()
    
    
        self.helper(i + 1, curComb, combs, nums, target)