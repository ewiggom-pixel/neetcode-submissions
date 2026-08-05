class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        # idea is that this dp but we either inlcude or not include the answer as we go throigh it. I also think that two pointers would work here for O(N): Yes it Kadane Algo it looks like but how do we do it with negative bc a negative times a negatative is positive. If we keep a min then we know if a n evil negative will fuck with the result

        result = nums[0]
        min_pro = 1 
        max_pro = 1
        for num in nums:
            temp = max_pro * num
            max_pro = max(max_pro * num, num* min_pro, num)
            min_pro = min(temp, num * min_pro, num)
            result = max(result, max_pro)
        return result
        

        