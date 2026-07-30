class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]

        for num in nums:
            result += [number + [num] for number in result]

        return result