class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda pair:pair[0])

        result = [intervals[0]]

        for interval in intervals:

            lastEnd = result[-1][1]

            if interval[0] <= lastEnd:
                result[-1][1] = max(lastEnd, interval[1])
            else: result.append(interval)
        
        return result