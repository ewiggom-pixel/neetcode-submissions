class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        res = [0] * n
        
        max1 = -1 

        for i in range((n-1), -1, -1):
            res[i] = max1
            max1 = max(max1, arr[i])
        return res