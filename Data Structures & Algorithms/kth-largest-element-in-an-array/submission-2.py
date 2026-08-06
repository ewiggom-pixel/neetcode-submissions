class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        answer = []
        count = 0
        
        
        if len(nums) == 0:
            return 0


        for i in range(len(nums)):
            if count < k:
                heapq.heappush(answer, nums[i])
                count += 1
            elif answer[0] <  nums[i]:
                heapq.heappop(answer)
                heapq.heappush(answer, nums[i])
             
             

        return answer[0] 