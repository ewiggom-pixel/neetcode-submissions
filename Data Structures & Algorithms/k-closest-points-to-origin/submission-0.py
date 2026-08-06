class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        if len(points) == 0:
            return []
        
        arr = []
    

        for i in range(len(points)):
            arr.append(((points[i][0])**2 + (points[i][1])**2, points[i]))
        
        heapq.heapify(arr)
    
        answer  = []
        for i in range(k):
            answer.append(heapq.heappop(arr)[1])
            
        return answer