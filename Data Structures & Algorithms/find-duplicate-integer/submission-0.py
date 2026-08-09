class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        stuff = set()

        for i in range(len(nums)):

            if nums[i] in stuff:
                return nums[i]
            else:
                stuff.add(nums[i]
                )