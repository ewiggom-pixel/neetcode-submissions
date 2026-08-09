class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      #slow way with hash set 
        stuff = set()

        for i in range(len(nums)):

            if nums[i] in stuff:
                return nums[i]
            else:
                stuff.add(nums[i]
                )
        #fast way with pointer sorry I mean with O(1) space

        slow = 0
        fast = 0

        n = len(nums)

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        pointer = 0
        while True:
            slow = nums[slow]
            slow2 = nums[pointer]
            if slow == slow2:
                return slow

