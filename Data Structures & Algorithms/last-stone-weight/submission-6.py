class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        print(max_heap)
        
        
        while len(max_heap) >= 2:
            temp1 = heapq.heappop(max_heap)
            temp2 = heapq.heappop(max_heap)

            if temp1 > temp2:
                heapq.heappush(max_heap,(temp2- temp1))
            if temp1 < temp2:
                heapq.heappush(max_heap,(temp1- temp2))
            
            print(max_heap)
        
   
        if len(max_heap) != 0:
            return max_heap[0] * -1
        else:
            return 0