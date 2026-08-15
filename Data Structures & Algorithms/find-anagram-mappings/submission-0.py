class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        index = {}
        for i in range(len(nums2)):
            index[nums2[i]] = i

        result = [0] * len(nums1)

        for i in range(len(nums1)):
            result[i] = index[nums1[i]]

        return result
        
        

