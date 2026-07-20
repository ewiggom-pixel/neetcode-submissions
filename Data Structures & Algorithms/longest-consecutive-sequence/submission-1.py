class Solution: 
    def longestConsecutive(self, nums: List[int]) -> int:
        curent_num = 0
        longest_streak = 0
        zero_streak = 0 
        set_of_nums = set(nums)

        for num in set_of_nums:
            if num-1 not in set_of_nums:
                curent_num = num
                current_steak = 1
                while curent_num +1 in set_of_nums:
                    curent_num += 1
                    current_steak += 1
                longest_streak = max(longest_streak,current_steak)
        
        return longest_streak


