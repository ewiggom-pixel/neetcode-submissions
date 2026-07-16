class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        numbers = [0]
        real_counter = 0 
        counter = 0 
        for i in range(len(nums)):
            if nums[i] != 1:
                counter = 0
            if nums[i] == 1:
                counter += 1
                numbers.append(counter)
            real_counter = max(numbers)
            if real_counter is None:
                return 0
        return real_counter 
