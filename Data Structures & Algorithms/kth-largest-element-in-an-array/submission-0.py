class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 0:
            return 0


        nums = [-x for x in nums]

        heapq.heapify(nums)

        for i in range(k-1):
             heapq.heappop(nums)

        return nums[0] * -1