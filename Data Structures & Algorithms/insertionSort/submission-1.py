# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []
        if len(pairs) == 0:
            return []
        result.append(list(pairs))
        for i in range(1,len(pairs)):
            key = pairs[i]
            j = i-1
            while j>= 0 and key.key < pairs[j].key:
               temp = pairs[j+1]
               pairs[j+1] = pairs[j]
               pairs[j]= temp
               j -= 1
            result.append(list(pairs))
        
        return result 
