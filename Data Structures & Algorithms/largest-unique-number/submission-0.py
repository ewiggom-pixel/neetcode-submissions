class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        large = -1

        hash_map = Counter(nums)
        for i in range(len(nums)):
            if nums[i] > large and hash_map[nums[i]]== 1:
                large = nums[i]
        return large

            