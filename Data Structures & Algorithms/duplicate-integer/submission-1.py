class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = set(nums)
        if len(answer) != len(nums):
            return True
        else: 
            return False