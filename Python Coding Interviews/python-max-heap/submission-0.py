import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    results= []
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)
    while max_heap:
        top = top = results.append(-heapq.heappop(max_heap))
    return results





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
