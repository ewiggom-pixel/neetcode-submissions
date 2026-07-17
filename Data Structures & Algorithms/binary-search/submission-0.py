class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        Left, Right = 0, len(nums) - 1

        while Left <= Right:

            mid = (Left + Right) // 2

            if target > nums[mid]:
                Left = mid  + 1
            elif target < nums[mid]:
                Right = mid - 1
            else:
                return mid


        return -1   