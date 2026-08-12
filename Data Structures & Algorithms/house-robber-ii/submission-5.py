class Solution:
    def rob(self, nums: List[int], cahce = None) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
         
        def rob_linear(houses):
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]

            house = [0] * len(houses)

            house[0] = houses[0]
            house[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                house[i] = max(house[i-1], house[i-2] + houses[i])
            return house[-1]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))