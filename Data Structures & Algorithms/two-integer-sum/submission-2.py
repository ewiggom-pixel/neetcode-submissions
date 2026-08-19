class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_set = {}

        for i, num in enumerate(nums):
            stuff = target - num
            if stuff in hash_set:
                return [hash_set[stuff], i]
            hash_set[num] = i
        
        return []
            