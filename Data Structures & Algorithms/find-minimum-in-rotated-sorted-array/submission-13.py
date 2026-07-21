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
            if nums[mid] < nums[R]:
                R = mid 
            else: 
                L = mid + 1 
        return nums[L]
                
            
        

        



