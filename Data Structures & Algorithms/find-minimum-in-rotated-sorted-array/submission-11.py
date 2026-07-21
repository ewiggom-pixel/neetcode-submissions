class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        L = 0
        R = len(nums) - 1 
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        while L < R:

            mid = (L+R) // 2
            print(mid)
            if nums[mid] < nums[R]:
                R = mid 
            else: 
                L = mid + 1 
            if nums[L] == nums[R]:
                return nums[L]
                
            
        

        



