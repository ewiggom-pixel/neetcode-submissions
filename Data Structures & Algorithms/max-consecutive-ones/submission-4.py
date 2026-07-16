class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        real_counter = 0 
        counter = 0 
        for num in nums:
            counter += 1
            if num != 1:
                counter = 0 
            real_counter = max(real_counter,counter)
        return real_counter