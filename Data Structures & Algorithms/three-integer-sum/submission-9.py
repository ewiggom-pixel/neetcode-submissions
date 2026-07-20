class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        nums.sort()
        results = []
        while i < len(nums):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                        r -= 1
            

                elif threesum < 0:
                        l += 1

                else: 
                    results.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r-= 1
            i += 1
        return results