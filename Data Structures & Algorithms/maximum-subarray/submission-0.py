class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = nums[0]
        cur_sum = 0

        for num in nums: 
            cur_sum = max(cur_sum,0)
            cur_sum += num
            result = max(result,cur_sum)

        return result