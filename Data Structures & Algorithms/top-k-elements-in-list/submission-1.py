class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]

        for value, freq in counts.items():
            bucket[freq].append(value)
        
        result = []
        for freq in range(len(bucket) -1, 0, -1):
            for value in bucket[freq]:
                result.append(value)
            if len(result) == k:
                return result
