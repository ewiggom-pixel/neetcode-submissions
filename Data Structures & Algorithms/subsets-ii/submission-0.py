class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset, curset =[], []

        
        def helper(i, nums, subset, curset):
            if i >= len(nums):
                subset.append(curset.copy())
                return

            curset.append(nums[i])
            helper(i+1, nums, subset, curset)
            curset.pop()

            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            helper(i+1, nums, subset, curset)
        
        helper(0, nums, subset, curset)
        return subset



