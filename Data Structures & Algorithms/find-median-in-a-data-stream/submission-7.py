class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap =  []
        

    def addNum(self, num: int) -> None:
            mx = self.max_heap
            mi = self.min_heap

            if len(mx) == 0 or num <= -1 * mx[0]:
                heapq.heappush(mx, -1 * num)
            else:
                heapq.heappush(mi, num)

   
            if len(mx) - len(mi) >= 2:
                heapq.heappush(mi, -1 * heapq.heappop(mx))
            if len(mi) - len(mx) >= 1:
                heapq.heappush(mx, -1 * heapq.heappop(mi))
        

    def findMedian(self) -> float:
        if len(self.min_heap) == 0 and len(self.max_heap) == 0:
            return 0.0
        if len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0] ) / 2.0

        